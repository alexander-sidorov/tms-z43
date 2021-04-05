import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

_application = get_asgi_application()


async def application(scope, receive, send):
    if scope["path"].startswith("/api"):
        from api.asgi import app

        return await app(scope, receive, send)
    else:
        return await _application(scope, receive, send)
