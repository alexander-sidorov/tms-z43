from typing import Dict

from main.custom_types import HandlerT
from main.custom_types import RequestT
from tasks.lesson01 import task103
from tasks.lesson03 import task301
from tasks.lesson03 import task302
from tasks.lesson03 import task303
from tasks.lesson03 import task309

from . import error_test
from . import index
from .system_handlers import handle_404
from .system_handlers import handle_500

urlpatterns: Dict[str, HandlerT] = {
    "/": index.handler,
    "/e/": error_test.handler,
    "/tasks/1/103/": task103.handler,
    "/tasks/3/301/": task301.handler,
    "/tasks/3/302/": task302.handler,
    "/tasks/3/303/": task303.handler,
    "/tasks/3/309/": task309.handler,
}


def get_handler(request: RequestT) -> HandlerT:
    handler = urlpatterns.get(request.path, handle_404)

    return handler
