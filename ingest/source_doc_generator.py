import ast
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Sequence


@dataclass
class DocCardItem:
    info_type: Optional[str]
    variable_name: Optional[str]
    code_file: Optional[str]
    describe: str


class SourceDocGenerator:
    TABLE_COLUMNS = {
        "props": ["属性", "说明", "类型", "默认值"],
        "function": ["方法名", "说明", "参数"],
        "event": ["事件名", "说明", "回调参数"],
        "slots": ["插槽名", "说明", "子标签"],
    }
    TYPE_LABELS = {
        "props": "属性 Props",
        "function": "方法 Methods",
        "event": "事件 Events",
        "slots": "插槽 Slots",
    }
    TYPE_DESCRIPTIONS = {
        "props": "组件支持的属性配置，用于控制组件的行为和外观。",
        "function": "组件暴露的方法，可通过 ref 调用。",
        "event": "组件触发的事件，可通过 @ 或 v-on 监听。",
        "slots": "组件提供的插槽，用于自定义内容渲染。",
    }
    COMMON_PROP_DESCRIPTIONS = {
        "v-model": "双向绑定值，用于获取和设置组件的当前值",
        "modelValue": "组件绑定值，配合 v-model 使用",
        "disabled": "是否禁用组件，禁用后无法进行交互",
        "clearable": "是否显示清除按钮，点击可清空当前值",
        "placeholder": "占位提示文字，在无输入时显示",
        "width": "组件宽度，支持像素值或百分比",
        "height": "组件高度，支持像素值或百分比",
        "size": "组件尺寸大小，可选 large/default/small",
        "type": "组件类型或模式",
        "data": "数据源，用于渲染组件内容",
        "loading": "是否显示加载状态",
        "filterable": "是否支持筛选/搜索功能",
        "multiple": "是否支持多选模式",
        "teleported": "是否将弹出层添加到 body 中，避免定位问题",
    }
    INVALID_TITLE_PATTERNS = [
        re.compile(r"^\{\{.*\}\}$"),
        re.compile(r"^\$\w+\(.*\)$"),
        re.compile(r"^index\d*$", re.IGNORECASE),
        re.compile(r"^test\d*$", re.IGNORECASE),
        re.compile(r"^demo\d*$", re.IGNORECASE),
        re.compile(r"^example\d*$", re.IGNORECASE),
        re.compile(r"^[a-z]+\d+$", re.IGNORECASE),
        re.compile(r"^[\u4e00-\u9fa5]{1}$"),
    ]
    COMPONENT_CATEGORY_DEFAULT = {"category": "other", "tags": [], "aliases": []}
    COMPONENT_CATEGORIES = {
        "Input": {"category": "form", "tags": ["输入框", "表单", "文本输入"], "aliases": ["Input", "输入"]},
        "Select": {"category": "form", "tags": ["选择器", "表单", "下拉选择"], "aliases": ["Select", "选择"]},
        "Tables": {"category": "data", "tags": ["表格", "数据展示"], "aliases": ["Tables", "表格"]},
        "Dialog": {"category": "feedback", "tags": ["对话框", "弹窗"], "aliases": ["Dialog", "弹窗"]},
    }

    def __init__(self, source_root: str, docs_root: str):
        self.source_root = Path(source_root)
        self.docs_root = Path(docs_root)
        self.output_dir = self.docs_root
        self.views_dir = self.source_root / "src" / "views"
        self.code_dir = self.source_root / "src" / "code"
        self.exclude_dirs = {"components"}
        self.split_threshold = 500
        self.max_title_length = 50

    def generate(self) -> Dict[str, object]:
        if not self.source_root.exists() or not self.views_dir.exists():
            return {"generated_files": [], "count": 0, "skipped": True}

        self.output_dir.mkdir(parents=True, exist_ok=True)
        vue_files = self._scan_vue_files(self.views_dir)
        generated_files: List[str] = []

        for vue_file in vue_files:
            result = self._process_vue_file(vue_file)
            if result is None:
                continue

            output_path = self.output_dir / f"{vue_file.stem}.md"
            output_path.write_text(result["markdown"], encoding="utf-8")
            generated_files.append(str(output_path))

            for split_file in result.get("split_files", []):
                split_path = self.output_dir / split_file["name"]
                split_path.write_text(split_file["content"], encoding="utf-8")
                generated_files.append(str(split_path))

        return {
            "generated_files": generated_files,
            "count": len(generated_files),
            "skipped": False,
        }

    def _scan_vue_files(self, start_dir: Path) -> List[Path]:
        results: List[Path] = []
        for file_path in start_dir.rglob("*.vue"):
            if any(part in self.exclude_dirs for part in file_path.parts):
                continue
            results.append(file_path)
        return sorted(results)

    def _process_vue_file(self, file_path: Path) -> Optional[Dict[str, object]]:
        content = file_path.read_text(encoding="utf-8", errors="ignore")
        doc_cards = self._extract_doc_cards(content)
        if not doc_cards:
            return None

        variables = self._extract_variable_declarations(content)
        valid_doc_cards: List[Dict[str, object]] = []
        code_examples: List[Dict[str, str]] = []
        for card in doc_cards:
            if card.code_file:
                code_content = self._read_code_file(card.code_file)
                if code_content:
                    code_examples.append(
                        {
                            "code_file": card.code_file,
                            "describe": card.describe,
                            "code": code_content,
                        }
                    )

            if not card.info_type or not card.variable_name:
                continue
            array_str = variables.get(card.variable_name)
            if not array_str:
                continue
            rows = self._extract_sub_arrays(array_str)
            if not rows:
                continue
            valid_doc_cards.append(
                {
                    "type": card.info_type,
                    "variable_name": card.variable_name,
                    "data": rows,
                }
            )

        if not valid_doc_cards:
            return None

        hpoints = self._extract_hpoints(content)
        markdown = self._generate_markdown(file_path.stem, valid_doc_cards, code_examples, hpoints)
        line_count = len(markdown.splitlines())
        split_files: List[Dict[str, str]] = []
        if line_count > self.split_threshold and len(code_examples) > 5:
            groups = self._group_examples_by_function(code_examples)
            for group_name, group_data in groups.items():
                if not group_data["examples"]:
                    continue
                split_files.append(
                    {
                        "name": f"{file_path.stem}-{group_name}.md",
                        "content": self._generate_split_markdown(
                            file_path.stem,
                            group_name,
                            group_data["name"],
                            group_data["examples"],
                            hpoints,
                        ),
                    }
                )

        return {"markdown": markdown, "split_files": split_files}

    def _extract_variable_declarations(self, content: str) -> Dict[str, str]:
        script_match = re.search(r"<script[^>]*>([\s\S]*?)</script>", content)
        if not script_match:
            return {}
        script_content = script_match.group(1)
        var_decl_regex = re.compile(r"(?:const|let|var)\s+(\w+)\s*=\s*\[")
        variables: Dict[str, str] = {}
        for match in var_decl_regex.finditer(script_content):
            var_name = match.group(1)
            start_idx = match.end() - 1
            end_idx = self._find_matching_bracket(script_content, start_idx, "[", "]")
            if end_idx is None:
                continue
            variables[var_name] = script_content[start_idx:end_idx + 1]
        return variables

    def _extract_sub_arrays(self, array_str: str) -> List[List[str]]:
        inner = array_str.strip()
        if len(inner) < 2 or not inner.startswith("[") or not inner.endswith("]"):
            return []
        content = inner[1:-1]
        result: List[List[str]] = []
        depth = 0
        start = -1
        for idx, char in enumerate(content):
            if char == "[":
                if depth == 0:
                    start = idx
                depth += 1
            elif char == "]":
                depth -= 1
                if depth == 0 and start != -1:
                    sub = content[start:idx + 1]
                    parsed = self._parse_array_content(sub)
                    if parsed:
                        result.append(parsed)
                    start = -1
        return result

    def _parse_array_content(self, array_str: str) -> List[str]:
        try:
            data = ast.literal_eval(array_str)
            if not isinstance(data, list):
                return []
            return [str(item) for item in data]
        except Exception:
            return []

    def _extract_doc_cards(self, content: str) -> List[DocCardItem]:
        doc_cards: List[DocCardItem] = []
        doc_card_regex = re.compile(r"<DocCard([^>]*)(?:/?>|>([\s\S]*?)</DocCard>)")
        for match in doc_card_regex.finditer(content):
            attrs = match.group(1) or ""
            inner_content = match.group(2) or ""
            doc_cards.append(
                DocCardItem(
                    info_type=self._extract_attr(attrs, "infoType"),
                    variable_name=self._extract_attr(attrs, "infoData"),
                    code_file=self._extract_attr(attrs, "codeFile"),
                    describe=self._extract_describe(attrs, inner_content),
                )
            )
        return doc_cards

    def _extract_attr(self, attrs: str, name: str) -> Optional[str]:
        patterns = [
            rf"\b{name}=[\"']([^\"']+)[\"']",
            rf":{name}=[\"']'([^']+)'[\"']",
            rf":{name}=\"'([^']+)'\"",
            rf":{name}=[\"']?([^\"'\s>]+)[\"']?",
        ]
        for pattern in patterns:
            m = re.search(pattern, attrs)
            if m:
                return m.group(1).strip()
        return None

    def _extract_describe(self, attrs: str, inner_content: str) -> str:
        describe = self._extract_attr(attrs, "describe") or ""
        slot_match = re.search(r"<template\s+#describe[^>]*>([\s\S]*?)</template>", inner_content)
        if slot_match:
            describe = re.sub(r"<[^>]+>", " ", slot_match.group(1))
            describe = re.sub(r"\s+", " ", describe).strip()
        return describe

    def _read_code_file(self, code_file_path: str) -> Optional[str]:
        normalized = code_file_path.strip().lstrip("/")
        full_path = self.code_dir / f"{normalized}.xhtml"
        if not full_path.exists():
            return None
        return full_path.read_text(encoding="utf-8", errors="ignore")

    def _extract_hpoints(self, content: str) -> Dict[str, List[str]]:
        titles: List[str] = []
        outlinks: List[str] = []
        for match in re.finditer(r"<HPoint[^>]*>", content):
            tag = match.group(0)
            title = self._extract_attr(tag, "title")
            outlink = self._extract_attr(tag, "outlink")
            if title:
                titles.append(title)
            if outlink:
                outlinks.append(outlink)
        return {"titles": titles, "outlinks": outlinks}

    def _generate_markdown(
        self,
        component_name: str,
        doc_cards_data: List[Dict[str, object]],
        code_examples: List[Dict[str, str]],
        hpoints: Dict[str, List[str]],
    ) -> str:
        md: List[str] = []
        md.append(self._generate_frontmatter(component_name, hpoints))
        md.append(f"# {component_name} 组件文档")
        md.append("")
        if hpoints["titles"]:
            md.append(f"> {hpoints['titles'][0]}")
            md.append("")

        category_info = self.COMPONENT_CATEGORIES.get(component_name, self.COMPONENT_CATEGORY_DEFAULT)
        tags = category_info.get("tags", [])
        if tags:
            md.append(f"**分类**: {category_info.get('category', 'other')} | **标签**: {'、'.join(tags)}")
            md.append("")

        if code_examples:
            md.append("## 使用示例")
            md.append("")
            for idx, example in enumerate(code_examples):
                title = self._clean_title(example.get("describe", ""), example.get("code_file", ""), idx)
                md.append(f"### {title}")
                md.append("")
                md.append("```vue")
                md.append(example.get("code", "").strip())
                md.append("```")
                md.append("")

        grouped = {"props": [], "function": [], "event": [], "slots": [], "default": []}
        for item in doc_cards_data:
            item_type = str(item.get("type", "default"))
            if item_type in grouped:
                grouped[item_type].extend(item.get("data", []))
            else:
                grouped["default"].extend(item.get("data", []))

        for item_type in ("props", "function", "event", "slots"):
            rows = grouped[item_type]
            if not rows:
                continue
            md.append(f"## {self.TYPE_LABELS[item_type]}")
            md.append("")
            md.append(self.TYPE_DESCRIPTIONS[item_type])
            md.append("")
            headers = self.TABLE_COLUMNS[item_type]
            md.append(self._generate_markdown_table(headers, rows, is_props=item_type == "props"))
            md.append("")

        if grouped["default"]:
            md.append("## 其他信息")
            md.append("")
            rows = grouped["default"]
            if len(rows) > 1:
                headers = [str(item) for item in rows[0]]
                md.append(self._generate_markdown_table(headers, rows[1:], is_props=False))
            md.append("")

        if hpoints["outlinks"]:
            md.append("## 相关链接")
            md.append("")
            for link in hpoints["outlinks"]:
                md.append(f"- [Element Plus 文档]({link})")
            md.append("")

        return "\n".join(md).strip() + "\n"

    def _generate_frontmatter(self, component_name: str, hpoints: Dict[str, List[str]]) -> str:
        category_info = self.COMPONENT_CATEGORIES.get(component_name, self.COMPONENT_CATEGORY_DEFAULT)
        tags = category_info.get("tags", []) or [component_name]
        aliases = category_info.get("aliases", []) or [component_name]
        lines = [
            "---",
            f"component: {component_name}",
            f"category: {category_info.get('category', 'other')}",
            f"tags: [{', '.join(tags)}]",
            f"aliases: [{', '.join(aliases)}]",
            "version: 1.0.0",
        ]
        if hpoints["titles"]:
            desc = hpoints["titles"][0].replace('"', '\\"')
            lines.append(f'description: "{desc}"')
        lines.append("---")
        lines.append("")
        return "\n".join(lines)

    def _generate_markdown_table(self, headers: Sequence[str], rows: Sequence[Sequence[str]], is_props: bool) -> str:
        if not headers or not rows:
            return ""
        lines = []
        lines.append(f"| {' | '.join(headers)} |")
        lines.append(f"| {' | '.join(['---'] * len(headers))} |")
        for row in rows:
            cells: List[str] = []
            for idx, header in enumerate(headers):
                value = str(row[idx]) if idx < len(row) else "--"
                if is_props and idx == 1 and row:
                    value = self._enhance_property_description(str(row[0]), value)
                value = value.replace("|", "\\|").replace("\n", " ")
                cells.append(value)
            lines.append(f"| {' | '.join(cells)} |")
        return "\n".join(lines)

    def _enhance_property_description(self, prop_name: str, original: str) -> str:
        common = self.COMMON_PROP_DESCRIPTIONS.get(prop_name)
        if common and original and original not in {"--", "——"} and len(original) < 20:
            return f"{original}。{common}"
        if common and (not original or original in {"--", "——"}):
            return common
        return original or "--"

    def _clean_title(self, title: str, code_file: str, index: int) -> str:
        if not title:
            return self._fallback_title(code_file, index)
        cleaned = title.strip()
        for pattern in self.INVALID_TITLE_PATTERNS:
            if pattern.match(cleaned):
                return self._fallback_title(code_file, index)
        if len(cleaned) > self.max_title_length:
            truncated = cleaned[: self.max_title_length]
            punct_idx = max(
                truncated.rfind("。"),
                truncated.rfind("，"),
                truncated.rfind(" "),
                truncated.rfind(","),
                truncated.rfind("."),
            )
            if punct_idx > int(self.max_title_length * 0.5):
                return truncated[:punct_idx].strip()
            return f"{truncated.strip()}..."
        return cleaned

    def _fallback_title(self, code_file: str, index: int) -> str:
        if code_file:
            file_name = code_file.split("/")[-1]
            humanized = re.sub(r"([A-Z])", r" \1", file_name).strip()
            return f"示例：{humanized or file_name}"
        return f"示例 {index + 1}"

    def _group_examples_by_function(self, code_examples: List[Dict[str, str]]) -> Dict[str, Dict[str, object]]:
        groups: Dict[str, Dict[str, object]] = {
            "basic": {"name": "基础用法", "examples": []},
            "advanced": {"name": "高级用法", "examples": []},
            "custom": {"name": "自定义配置", "examples": []},
            "other": {"name": "其他示例", "examples": []},
        }
        for idx, example in enumerate(code_examples):
            title = (example.get("describe") or "").lower()
            code_file = (example.get("code_file") or "").lower()
            if ("基础" in title) or ("基本" in title) or ("basic" in title) or ("basic" in code_file) or idx < 2:
                groups["basic"]["examples"].append(example)
            elif ("高级" in title) or ("复杂" in title) or ("advanced" in title) or ("advanced" in code_file):
                groups["advanced"]["examples"].append(example)
            elif ("自定义" in title) or ("配置" in title) or ("custom" in title) or ("custom" in code_file):
                groups["custom"]["examples"].append(example)
            else:
                groups["other"]["examples"].append(example)
        return groups

    def _generate_split_markdown(
        self,
        component_name: str,
        group_name: str,
        group_label: str,
        examples: List[Dict[str, str]],
        hpoints: Dict[str, List[str]],
    ) -> str:
        category_info = self.COMPONENT_CATEGORIES.get(component_name, self.COMPONENT_CATEGORY_DEFAULT)
        tags = category_info.get("tags", []) + [group_name]
        aliases = category_info.get("aliases", []) or [component_name]
        md = [
            "---",
            f"component: {component_name}",
            f"submodule: {group_name}",
            f"category: {category_info.get('category', 'other')}",
            f"tags: [{', '.join(tags)}]",
            f"aliases: [{', '.join(aliases)}]",
            "version: 1.0.0",
            "---",
            "",
            f"# {component_name} - {group_label}",
            "",
        ]
        if hpoints["titles"]:
            md.append(f"> {hpoints['titles'][0]}")
            md.append("")
        md.append("## 使用示例")
        md.append("")
        for idx, example in enumerate(examples):
            title = self._clean_title(example.get("describe", ""), example.get("code_file", ""), idx)
            md.append(f"### {title}")
            md.append("")
            md.append("```vue")
            md.append(example.get("code", "").strip())
            md.append("```")
            md.append("")
        return "\n".join(md).strip() + "\n"

    @staticmethod
    def _find_matching_bracket(text: str, start: int, left: str, right: str) -> Optional[int]:
        depth = 0
        in_string = False
        string_char = ""
        escape = False
        for idx in range(start, len(text)):
            ch = text[idx]
            if in_string:
                if escape:
                    escape = False
                elif ch == "\\":
                    escape = True
                elif ch == string_char:
                    in_string = False
                continue
            if ch in {"'", '"'}:
                in_string = True
                string_char = ch
                continue
            if ch == left:
                depth += 1
            elif ch == right:
                depth -= 1
                if depth == 0:
                    return idx
        return None
