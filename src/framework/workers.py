from uvicorn.workers import UvicornWorker


class AsyncioUvicornWorker(UvicornWorker):
    CONFIG_KWARGS = {
        "http": "h11",
        "lifespan": "off",
        "loop": "asyncio",
    }
