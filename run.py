import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "index:app",
        reload=True,
        reload_dirs=["connectors", "runtime", "retrieve", "ingest", "indexing"],
    )
