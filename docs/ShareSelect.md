---
component: ShareSelect
category: other
tags: [ShareSelect]
aliases: [ShareSelect]
version: 1.0.0
description: "Share Select基础用法"
---

# ShareSelect 组件文档

> Share Select基础用法

## 使用示例

### Share Select 基础用法

```vue
<template>
  <pacvue-share-select
    ref="homeTagOption"
    v-model="tagIds"
    :data="treeTagOption"
    :props="{ label: 'label', value: 'id', children: 'children' }"
    @clear="clearTags"
    style="width: 400px"
    placeholder="Campaign tag"
    clearable
  >
  </pacvue-share-select>
</template>

<script setup>
  import { ref } from 'vue'
  var tagIds = ref([])
  var tagPropMap = ref({ id: 'id', label: 'label', children: 'children' })
  var visibleTagChange = () => {}
  var clearTags = () => {}
  var treeTagOption = ref([])
  treeTagOption.value = formatCampaignTag([
    { label: 'AMZ Search', id: 'AMZ Search', children: [], shareTagId: null },
    {
      label: 'Citrus',
      id: 'Citrus',
      children: [
        {
          label: '123',
          id: 'Citrus-1578659337436401665',
          children: [
            { label: '1', id: 'Citrus-1578664566038990849', children: [], shareTagId: '' },
            { label: '12333', id: 'Citrus-1589456417410306049', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'SY-CampaignTag1125-01',
          id: 'Citrus-1596057849254371330',
          children: [
            { label: 'SY-CampaignSubTag1125-01', id: 'Citrus-1596058110458847233', children: [], shareTagId: '' },
            { label: 'SY-CampaignSubTag1125-02', id: 'Citrus-1596058110517567490', children: [], shareTagId: '' },
            { label: 'SY-CampaignSubTag1125-03', id: 'Citrus-1596058110584676354', children: [], shareTagId: '' },
            { label: 'SY-CampaignSubTag1125-04', id: 'Citrus-1596058110651785218', children: [], shareTagId: '' },
            { label: 'SY-CampaignSubTag1125-05', id: 'Citrus-1596058110718894081', children: [], shareTagId: '' },
            { label: '列表addSY-CampaignSubTag1125-01', id: 'Citrus-1596065912006893570', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'SY-CampaignTag1125-02', id: 'Citrus-1596057934264524801', children: [], shareTagId: '' },
        { label: 'SY-CampaignTag1125-03', id: 'Citrus-1596057934402936833', children: [], shareTagId: '' },
        { label: 'SY-CampaignTag1125-04', id: 'Citrus-1596057934340022273', children: [], shareTagId: '' },
        {
          label: 'TBM112',
          id: 'Citrus-1497482024972193794',
          children: [{ label: '123', id: 'Citrus-1574317071691419650', children: [], shareTagId: '' }],
          shareTagId: ''
        },
        {
          label: 'TBM3123',
          id: 'Citrus-1497482024909279234',
          children: [
            { label: '1', id: 'Citrus-1552487729039138817', children: [], shareTagId: '' },
            { label: 'TBM301', id: 'Citrus-1497482097609150466', children: [], shareTagId: '' },
            { label: 'TBM302', id: 'Citrus-1497482097630121986', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'TBM411',
          id: 'Citrus-1497482024888307713',
          children: [
            { label: 'TBM4012', id: 'Citrus-1497482146061750274', children: [], shareTagId: '' },
            { label: 'TBM402', id: 'Citrus-1497482146082721794', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'TBM71',
          id: 'Citrus-1497482024657620993',
          children: [{ label: '123', id: 'Citrus-1574316388644818946', children: [], shareTagId: '' }],
          shareTagId: ''
        },
        {
          label: 'TBM755',
          id: 'Citrus-1497503513209475074',
          children: [
            { label: 'subtag1', id: 'Citrus-1497503574211432450', children: [], shareTagId: '' },
            { label: 'subtag2', id: 'Citrus-1497503606511767553', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'TTTT', id: 'Citrus-1497497490532864001', children: [], shareTagId: '' },
        {
          label: 'dawdd1',
          id: 'Citrus-1497500062643654658',
          children: [
            { label: '111', id: 'Citrus-1574573072755724289', children: [], shareTagId: '' },
            { label: '2', id: 'Citrus-1574239447307714562', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'e21e1', id: 'Citrus-1578669415385858050', children: [], shareTagId: '' },
        {
          label: 'uuuuu',
          id: 'Citrus-1497503991485960194',
          children: [
            { label: '111', id: 'Citrus-1574573926900568065', children: [], shareTagId: '' },
            { label: '222', id: 'Citrus-1574573926917345282', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        }
      ],
      shareTagId: null
    },
    {
      label: 'Criteo',
      id: 'Criteo',
      children: [
        {
          label: '  testC',
          id: 'Criteo-1560130828111491074',
          children: [{ label: '111-c', id: 'Criteo-1574573853968891905', children: [], shareTagId: '' }],
          shareTagId: ''
        },
        { label: '078', id: 'Criteo-1597399557255430146', children: [], shareTagId: '' },
        { label: '081001', id: 'Criteo-1557193203639353345', children: [], shareTagId: '' },
        { label: '089', id: 'Criteo-1600065996631904257', children: [], shareTagId: '' },
        { label: '090', id: 'Criteo-1600067380563480578', children: [], shareTagId: '1600067380467011585' },
        {
          label: '2222',
          id: 'Criteo-1536169332863852545',
          children: [{ label: '3335', id: 'Criteo-1537674196898996226', children: [], shareTagId: '' }],
          shareTagId: ''
        },
        { label: 'AAA', id: 'Criteo-1594574929927569409', children: [], shareTagId: '' },
        {
          label: 'Category',
          id: 'Criteo-1598599360193626113',
          children: [{ label: 'NNN', id: 'Criteo-1598599360206209025', children: [], shareTagId: '' }],
          shareTagId: '1598599359816138753'
        },
        {
          label: 'Match',
          id: 'Criteo-1533631704156082177',
          children: [
            { label: 'mmm', id: 'Criteo-1594570554513522689', children: [], shareTagId: '1594570554282835970' }
          ],
          shareTagId: '1533631703996698626'
        },
        {
          label: 'STT',
          id: 'Criteo-1592843474031407105',
          children: [
            { label: 'STTa', id: 'Criteo-1592843474048184322', children: [], shareTagId: '1592843473695862785' },
            { label: 'STTb', id: 'Criteo-1592843474043990017', children: [], shareTagId: '1592843473653919745' }
          ],
          shareTagId: '1592843473083494402'
        },
        { label: 'adamnew', id: 'Criteo-1593051736475496449', children: [], shareTagId: '1593051736282558465' },
        { label: 'dawang', id: 'Criteo-1597192867792781314', children: [], shareTagId: '1597192867285270530' },
        { label: 'dd accounting', id: 'Criteo-1560708269087436802', children: [], shareTagId: '' },
        { label: 'ljxin', id: 'Criteo-1574957302255517697', children: [], shareTagId: '' },
        {
          label: 'log test',
          id: 'Criteo-1587994020556234754',
          children: [
            { label: 'subTag 1', id: 'Criteo-1588005892266229762', children: [], shareTagId: '' },
            { label: 'subTag 2', id: 'Criteo-1588005904186441730', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'new1', id: 'Criteo-1593051736433553410', children: [], shareTagId: '1593051736269975553' },
        { label: 'new2', id: 'Criteo-1593051736492273666', children: [], shareTagId: '1593051736290947074' },
        { label: 'q2', id: 'Criteo-1562365024894164993', children: [], shareTagId: '' },
        {
          label: 'test-share tag',
          id: 'Criteo-1588434241124294657',
          children: [
            { label: '11', id: 'Criteo-1588434241195597825', children: [], shareTagId: '1588434240264462337' },
            { label: 'kw', id: 'Criteo-1588434241212375042', children: [], shareTagId: '1588434240302211073' },
            { label: 'test123', id: 'Criteo-1588434241162043393', children: [], shareTagId: '1588434240251879425' }
          ],
          shareTagId: '1588434240214130690'
        },
        { label: 'test0610', id: 'Criteo-1551497157052125185', children: [], shareTagId: '' },
        { label: 'testBudgetSchedulerTag', id: 'Criteo-1559493507142774785', children: [], shareTagId: '' },
        { label: 'testriy', id: 'Criteo-1560617433259618305', children: [], shareTagId: '' },
        {
          label: 'uk',
          id: 'Criteo-1550412527964180481',
          children: [
            { label: 'liverpool', id: 'Criteo-1552195142411608066', children: [], shareTagId: '' },
            { label: 'london', id: 'Criteo-1552195142352887810', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'wyy0816', id: 'Criteo-1559409499440541698', children: [], shareTagId: '' },
        {
          label: 'wyy_campaign_tag2',
          id: 'Criteo-1551497157001793537',
          children: [
            { label: 'wyy_campaign_tag2_subtag1', id: 'Criteo-1551497286169579522', children: [], shareTagId: '' },
            { label: 'wyy_campaign_tag2_subtag2', id: 'Criteo-1551497286161190914', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: '全新的tag111111111111111111111111111111',
          id: 'Criteo-1555125003863007234',
          children: [],
          shareTagId: ''
        },
        { label: '我是tag', id: 'Criteo-1555115686112448514', children: [], shareTagId: '' },
        {
          label: '我是全新的tag',
          id: 'Criteo-1554437680691859458',
          children: [
            { label: 'qq', id: 'Criteo-1554437730536968193', children: [], shareTagId: '' },
            { label: 'qq2', id: 'Criteo-1554437901735874562', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: '旧版campaign tag', id: 'Criteo-1556516596445143042', children: [], shareTagId: '' },
        {
          label: '欧洲足球联赛',
          id: 'Criteo-1594564173215531009',
          children: [
            { label: '哈哈1', id: 'Criteo-1594566093032357889', children: [], shareTagId: '1594566092721979393' },
            { label: '哈哈2', id: 'Criteo-1594566093023969282', children: [], shareTagId: '1594566092709396481' }
          ],
          shareTagId: '1594566092701007874'
        },
        { label: '测试linetearm的不同状态', id: 'Criteo-1554722340890136577', children: [], shareTagId: '' },
        {
          label: '测试ruletag',
          id: 'Criteo-1562365087565455362',
          children: [{ label: 'w', id: 'Criteo-1562365284399947777', children: [], shareTagId: '' }],
          shareTagId: ''
        },
        { label: '测试tag模式1111', id: 'Criteo-1556939804570255361', children: [], shareTagId: '' },
        { label: '测试增长-campaigntag', id: 'Criteo-1556584846264688642', children: [], shareTagId: '' }
      ],
      shareTagId: null
    },
    {
      label: 'Instacart',
      id: 'Instacart',
      children: [
        { label: '078', id: 'Instacart-4529', children: [], shareTagId: '' },
        { label: '089', id: 'Instacart-4550', children: [], shareTagId: '' },
        { label: '090', id: 'Instacart-4551', children: [], shareTagId: '1600067380467011585' },
        { label: '11111', id: 'Instacart-4179', children: [], shareTagId: '' },
        { label: '111111111111111111', id: 'Instacart-4548', children: [], shareTagId: '' },
        { label: '222', id: 'Instacart-4109', children: [], shareTagId: '' },
        { label: '7777771111', id: 'Instacart-4100', children: [], shareTagId: '' },
        {
          label: 'Category',
          id: 'Instacart-4535',
          children: [{ label: 'NNN', id: 'Instacart-4536', children: [], shareTagId: '' }],
          shareTagId: '1598599359816138753'
        },
        { label: 'GC', id: 'Instacart-4260', children: [], shareTagId: '' },
        { label: 'HHH2', id: 'Instacart-4078', children: [], shareTagId: '' },
        {
          label: 'Match',
          id: 'Instacart-3674',
          children: [
            { label: '22', id: 'Instacart-3856', children: [], shareTagId: '' },
            { label: '33', id: 'Instacart-4003', children: [], shareTagId: '' },
            { label: '44', id: 'Instacart-4004', children: [], shareTagId: '' },
            { label: 'match 1', id: 'Instacart-4007', children: [], shareTagId: '' },
            { label: 'match 2', id: 'Instacart-4512', children: [], shareTagId: '' },
            { label: 'match_sub2', id: 'Instacart-4008', children: [], shareTagId: '' },
            { label: 'mmm', id: 'Instacart-4511', children: [], shareTagId: '1594570554282835970' }
          ],
          shareTagId: '1533631703996698626'
        },
        {
          label: 'STT',
          id: 'Instacart-4496',
          children: [
            { label: 'STTa', id: 'Instacart-4498', children: [], shareTagId: '1592843473695862785' },
            { label: 'STTb', id: 'Instacart-4497', children: [], shareTagId: '1592843473653919745' }
          ],
          shareTagId: '1592843473083494402'
        },
        {
          label: 'Tag A',
          id: 'Instacart-4086',
          children: [
            { label: '11', id: 'Instacart-4353', children: [], shareTagId: '' },
            { label: '1111', id: 'Instacart-4354', children: [], shareTagId: '' },
            { label: 'Sub Tag A', id: 'Instacart-4088', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'Tag B',
          id: 'Instacart-4087',
          children: [
            { label: 'Sub Tag A', id: 'Instacart-4096', children: [], shareTagId: '' },
            { label: 'Sub Tag B', id: 'Instacart-4089', children: [], shareTagId: '' },
            { label: 'Sub Tag B22', id: 'Instacart-4108', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'TagBB',
          id: 'Instacart-4101',
          children: [
            { label: 'Sub Tag BA', id: 'Instacart-4107', children: [], shareTagId: '' },
            { label: 'Sub Tag BB', id: 'Instacart-4102', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'adamnew', id: 'Instacart-4499', children: [], shareTagId: '1593051736282558465' },
        { label: 'dawang', id: 'Instacart-4528', children: [], shareTagId: '1597192867285270530' },
        { label: 'jhhhhhhuuuiiiiiii', id: 'Instacart-4549', children: [], shareTagId: '' },
        { label: 'ljaaaaa', id: 'Instacart-4520', children: [], shareTagId: '' },
        {
          label: 'ljbudget',
          id: 'Instacart-4194',
          children: [
            { label: '111', id: 'Instacart-4195', children: [], shareTagId: '' },
            { label: '222', id: 'Instacart-4196', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'lj测试1', id: 'Instacart-4094', children: [], shareTagId: '' },
        { label: 'lj测试111111', id: 'Instacart-4532', children: [], shareTagId: '' },
        {
          label: 'lj测试2',
          id: 'Instacart-4095',
          children: [
            { label: 'Sub Tag A', id: 'Instacart-4097', children: [], shareTagId: '' },
            { label: 'Sub Tag B', id: 'Instacart-4098', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'lj测试222222222', id: 'Instacart-4533', children: [], shareTagId: '' },
        {
          label: 'lj测试campaigntype',
          id: 'Instacart-4517',
          children: [
            { label: '1', id: 'Instacart-4518', children: [], shareTagId: '' },
            { label: '2', id: 'Instacart-4519', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'lj测试tag.....', id: 'Instacart-4531', children: [], shareTagId: '' },
        { label: 'lj测试酷酷酷酷酷酷酷酷酷酷酷酷酷酷', id: 'Instacart-4547', children: [], shareTagId: '' },
        {
          label: 'new1',
          id: 'Instacart-4189',
          children: [
            { label: 'ga1', id: 'Instacart-4192', children: [], shareTagId: '' },
            { label: 'ga2', id: 'Instacart-4193', children: [], shareTagId: '' }
          ],
          shareTagId: '1593051736269975553'
        },
        { label: 'new2', id: 'Instacart-4190', children: [], shareTagId: '1593051736290947074' },
        { label: 'tagtagtag', id: 'Instacart-4204', children: [], shareTagId: '' },
        {
          label: 'test-share tag',
          id: 'Instacart-4453',
          children: [
            { label: '11', id: 'Instacart-4455', children: [], shareTagId: '1588434240264462337' },
            { label: 'kw', id: 'Instacart-4456', children: [], shareTagId: '1588434240302211073' },
            { label: 'test123', id: 'Instacart-4454', children: [], shareTagId: '1588434240251879425' }
          ],
          shareTagId: '1588434240214130690'
        },
        { label: 'test_whhh', id: 'Instacart-4198', children: [], shareTagId: '' },
        { label: 'test_whhhh', id: 'Instacart-4199', children: [], shareTagId: '' },
        { label: 'test_whhhhW', id: 'Instacart-4200', children: [], shareTagId: '' },
        {
          label: 'turnoff_stop',
          id: 'Instacart-4524',
          children: [
            { label: 'turnoff_stop-1', id: 'Instacart-4525', children: [], shareTagId: '' },
            { label: 'turnoff_stop-2', id: 'Instacart-4526', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'www',
          id: 'Instacart-4099',
          children: [
            { label: '1', id: 'Instacart-4521', children: [], shareTagId: '' },
            { label: '2', id: 'Instacart-4522', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'wyy-测试',
          id: 'Instacart-4513',
          children: [
            { label: 'wyy-测试-A', id: 'Instacart-4514', children: [], shareTagId: '' },
            { label: 'wyy-测试-B', id: 'Instacart-4515', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'wyytest',
          id: 'Instacart-4503',
          children: [
            { label: '3333', id: 'Instacart-4527', children: [], shareTagId: '' },
            { label: 'wyytest1118-1', id: 'Instacart-4504', children: [], shareTagId: '' },
            { label: 'wyytest1118-2', id: 'Instacart-4505', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy ',
          id: 'Instacart-4090',
          children: [
            {
              label: '11111111111111111111111111111111111111111111111111111',
              id: 'Instacart-4091',
              children: [],
              shareTagId: ''
            }
          ],
          shareTagId: ''
        },
        {
          label: '已存在父子无物料',
          id: 'Instacart-4285',
          children: [
            { label: '111', id: 'Instacart-4287', children: [], shareTagId: '' },
            { label: '222', id: 'Instacart-4288', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: '已存在父子有物料',
          id: 'Instacart-4286',
          children: [
            { label: '111', id: 'Instacart-4289', children: [], shareTagId: '' },
            { label: '222', id: 'Instacart-4290', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: '欧洲足球联赛',
          id: 'Instacart-4508',
          children: [
            { label: '哈哈1', id: 'Instacart-4510', children: [], shareTagId: '1594566092721979393' },
            { label: '哈哈2', id: 'Instacart-4509', children: [], shareTagId: '1594566092709396481' }
          ],
          shareTagId: '1594566092701007874'
        },
        { label: '测试campaign tageeeeeeeeeeeeeeeeeeeeeeeeeeeee', id: 'Instacart-4546', children: [], shareTagId: '' },
        {
          label: '线上不存在C',
          id: 'Instacart-4110',
          children: [
            { label: '线上不存在A', id: 'Instacart-4114', children: [], shareTagId: '' },
            { label: '线上不存在B', id: 'Instacart-4111', children: [], shareTagId: '' },
            { label: '线上不存在D', id: 'Instacart-4112', children: [], shareTagId: '' },
            { label: '线上不存在E', id: 'Instacart-4113', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        }
      ],
      shareTagId: null
    },
    {
      label: 'Walmart',
      id: 'Walmart',
      children: [
        { label: 'AAA', id: 'Walmart-6498', children: [], shareTagId: '' },
        { label: 'BBB', id: 'Walmart-6499', children: [], shareTagId: '' },
        {
          label: 'BMTest1018-2',
          id: 'Walmart-6392',
          children: [
            { label: '222', id: 'Walmart-6681', children: [], shareTagId: '' },
            { label: 'sub1', id: 'Walmart-6438', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'BMTest1018-3',
          id: 'Walmart-6650',
          children: [
            { label: '-3-sub1', id: 'Walmart-6651', children: [], shareTagId: '' },
            { label: '-s-sub2', id: 'Walmart-6652', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        { label: 'CT1A', id: 'Walmart-6533', children: [], shareTagId: '' },
        {
          label: 'JackTestTag01',
          id: 'Walmart-6148',
          children: [
            { label: 'Sub01', id: 'Walmart-6149', children: [], shareTagId: '' },
            { label: 'Sub02', id: 'Walmart-6150', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'JackTestTag02',
          id: 'Walmart-6151',
          children: [
            { label: 'SubTag03', id: 'Walmart-6152', children: [], shareTagId: '' },
            { label: 'SubTag04', id: 'Walmart-6153', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: 'Match',
          id: 'Walmart-5188',
          children: [
            { label: 'M1', id: 'Walmart-6112', children: [], shareTagId: '' },
            { label: 'mmm', id: 'Walmart-6691', children: [], shareTagId: '1594570554282835970' }
          ],
          shareTagId: '1533631703996698626'
        },
        { label: 'RTB', id: 'Walmart-6114', children: [], shareTagId: '' },
        { label: 'RTC', id: 'Walmart-6115', children: [], shareTagId: '' },
        {
          label: 'STT',
          id: 'Walmart-6643',
          children: [
            { label: 'STTa', id: 'Walmart-6645', children: [], shareTagId: '1592843473695862785' },
            { label: 'STTb', id: 'Walmart-6644', children: [], shareTagId: '1592843473653919745' }
          ],
          shareTagId: '1592843473083494402'
        },
        { label: 'adamnew', id: 'Walmart-6649', children: [], shareTagId: '1593051736282558465' },
        {
          label: 'new1',
          id: 'Walmart-6391',
          children: [
            { label: '1018-1sub1', id: 'Walmart-6393', children: [], shareTagId: '' },
            { label: '1018-2sub2', id: 'Walmart-6394', children: [], shareTagId: '' }
          ],
          shareTagId: '1593051736269975553'
        },
        { label: 'new2', id: 'Walmart-6534', children: [], shareTagId: '1593051736290947074' },
        {
          label: 'test-share tag',
          id: 'Walmart-6524',
          children: [
            { label: '11', id: 'Walmart-6526', children: [], shareTagId: '1588434240264462337' },
            { label: 'kw', id: 'Walmart-6527', children: [], shareTagId: '1588434240302211073' },
            { label: 'test123', id: 'Walmart-6525', children: [], shareTagId: '1588434240251879425' }
          ],
          shareTagId: '1588434240214130690'
        },
        {
          label: 'xjtest1',
          id: 'Walmart-6549',
          children: [{ label: '123', id: 'Walmart-6685', children: [], shareTagId: '' }],
          shareTagId: ''
        },
        {
          label: '欧洲足球联赛',
          id: 'Walmart-6682',
          children: [
            { label: '哈哈1', id: 'Walmart-6684', children: [], shareTagId: '1594566092721979393' },
            { label: '哈哈2', id: 'Walmart-6683', children: [], shareTagId: '1594566092709396481' }
          ],
          shareTagId: '1594566092701007874'
        },
        {
          label: '父tag',
          id: 'Walmart-6678',
          children: [
            { label: '子tag 1', id: 'Walmart-6679', children: [], shareTagId: '' },
            { label: '子tag2', id: 'Walmart-6680', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        },
        {
          label: '茶叶',
          id: 'Walmart-6686',
          children: [
            { label: '太湖翠竹', id: 'Walmart-6689', children: [], shareTagId: '' },
            { label: '毛尖', id: 'Walmart-6690', children: [], shareTagId: '' },
            { label: '碧螺春', id: 'Walmart-6687', children: [], shareTagId: '' },
            { label: '龙井', id: 'Walmart-6688', children: [], shareTagId: '' }
          ],
          shareTagId: ''
        }
      ],
      shareTagId: null
    }
  ])
  function formatCampaignTag(dataList, level) {
    dataList = dataList || []
    var result = []
    level = level || 0
    var shareSubList = []
    var shareTagInfo = {
      id: 'Share Tag',
      label: 'Share Tag',
      isShare: true,
      children: shareSubList
    }
    var shareTagMap = {}
    for (var i = 0; i < dataList.length; i++) {
      var dataItem = dataList[i]
      var shareTagId = dataItem.shareTagId
      var children = dataItem.children || []
      dataItem.children = children
      // 获取shareTag 数据
      var shareTagList = getShareTagList(children, shareTagMap)
      shareSubList.push(...shareTagList)
    }
    if (shareSubList.length) {
      dataList.push(shareTagInfo)
    }
    return dataList
  }
  function getShareTagList(dataList, shareTagMap) {
    var result = []
    shareTagMap = shareTagMap || {}
    for (var i = 0; i < dataList.length; i++) {
      var dataItem = dataList[i]
      var shareTagId = dataItem.shareTagId
      var children = dataItem.children || []
      // 获取shareTag 数据
      var shareTagList = getShareTagList(children, shareTagMap)
      if (children.length) {
        if (shareTagId && !shareTagMap[shareTagId]) {
          shareTagMap[shareTagId] = shareTagId
          result.push({
            id: shareTagId,
            label: dataItem.label,
            shareTagId: shareTagId,
            children: shareTagList
          })
        }
      } else {
        if (shareTagId && !shareTagMap[shareTagId]) {
          shareTagMap[shareTagId] = shareTagId
          result.push({
            id: shareTagId,
            label: dataItem.label,
            shareTagId: shareTagId
          })
        }
      }
    }
    return result
  }
</script>
```

## 属性 Props

组件支持的属性配置，用于控制组件的行为和外观。

| 属性 | 说明 | 类型 | 默认值 |
| --- | --- | --- | --- |
| labelInner | 内联显示标签 | String | -- |
| data | 数据列表。数据源，用于渲染组件内容 | Array | [] |
| showZero | 值为零时是否显示统计图标 | boolean | true |
| placeholder | placeholder。占位提示文字，在无输入时显示 | String | Select All |
| modelValue/v-model | 选中项绑定值 | Array\|String\|Number | [] |
| props | 配置选项，具体看下表 | Object | { value: 'value', label: 'label', children: 'children' } |
| titleFirst | 下拉框是否全选checkbox显示在关键词筛选input之上 | Boolean | true |
| treeDropdownWidth | 下拉框中tree的宽度 | String | 250px |
| dropDownWRatio | 下拉框宽度是引用元素宽度的比例 | Number | -- |
| hasSplitLine | 下拉框宽度是否有分界线 | Boolean | false |
| height | 触发元素的高度。组件高度，支持像素值或百分比 | String | 36px |
| disabled | 是否禁用。是否禁用组件，禁用后无法进行交互 | Boolean | false |
| disableCallback | 下拉框中每一项禁用时回调 | Function(node):Boolean | -- |
| showSelectAll | 是否显示全选 | Boolean | false |
| showGroupSelectAll | 是否显示分组全选 | Boolean | true |
| filterable | 是否显示过滤框。是否支持筛选/搜索功能 | Boolean | true |
| showItemTip | 是否显示item的tip | Boolean | false |
| showSelectAll | 是否显示全选功能 | Boolean | false |
| showGroupSelectAll | 是否显示分组全选功能 | Boolean | true |
| hasOperand | 是否有操作符选项功能 | Boolean | false |
| operandConfig | 操作符选项配置,一般用作配置props,如果没有则使用组件的props配置 | Object | -- |
| operandDisabled | 操作符选项是否禁用 | Boolean | false |
| operandValue | 操作符选项值 | String\|Number\|Array | -- |
| operandData | 操作符选项数据 | Array | -- |
| isHideEmptyTree | 是否隐藏分组下面的tree为空时，不显示tree | Boolean | false |
| clearable | 是否可以清空选项。是否显示清除按钮，点击可清空当前值 | Boolean | false |
| disabledList | 禁用节点列表 | Array | [] |
| enableWithPaused | 是否可以设置Paused状态的节点勾选状态 | Boolean | false |
| selectAllWithoutDisabled | 是否在全选操作中排除禁用的节点勾选 | Boolean | false |
| selectAllStateWithPause | 是否全选状态包括禁用节点 | Boolean | false |

## 方法 Methods

组件暴露的方法，可通过 ref 调用。

| 方法名 | 说明 | 参数 |
| --- | --- | --- |
| getSelection | 获取当前选中select的信息 | () => {groupName:{values:Array,data:Array,count:Number}} |

## 事件 Events

组件触发的事件，可通过 @ 或 v-on 监听。

| 事件名 | 说明 | 回调参数 |
| --- | --- | --- |
| change | 绑定值变化触发事件 | Function(value) |

## 插槽 Slots

组件提供的插槽，用于自定义内容渲染。

| 插槽名 | 说明 | 子标签 |
| --- | --- | --- |
| selectLabel | 选中显示的插槽内容,slotScop为{selectedNames, selectNodes, selectedValues} | -- |
| relationship | 自定义的操作符选项内容 | -- |
| groupItemLabel | 类别选项内容,slotScop为{item: Object} | -- |

