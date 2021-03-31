import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "project.asgi:application",
        host="localhost",
        log_level="debug",
        port=8000,
        reload=True,
    )
