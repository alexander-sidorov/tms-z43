import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "project.asgi:application",
        host="localhost",
        port=8000,
        log_level="debug",
    )
