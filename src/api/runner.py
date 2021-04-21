import uvicorn

from framework import dirs

if __name__ == "__main__":
    uvicorn.run(
        "project.asgi:application",
        host="localhost",
        log_level="debug",
        port=8000,
        reload=True,
        reload_dirs=[dirs.DIR_SRC],
    )
