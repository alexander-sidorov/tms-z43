from typing import Dict

from main.custom_types import HandlerT
from main.custom_types import RequestT
from tasks.lesson01 import task103
from tasks.lesson03 import task301
from tasks.lesson03 import task302
from tasks.lesson03 import task303
from tasks.lesson03 import task304
from tasks.lesson03 import task305
from tasks.lesson03 import task306
from tasks.lesson03 import task307
from tasks.lesson03 import task309
from tasks.lesson03 import task310
from tasks.lesson03 import task311
from tasks.lesson04 import task402

from . import error_test
from . import index
from .system_handlers import handle_404
from .system_handlers import handle_500

urlpatterns: Dict[str, HandlerT] = {
    "/": index.handler,
    "/api/v1/tasks/402/": task402.handler_api,
    "/e/": error_test.handler,
    "/tasks/1/103/": task103.handler,
    "/tasks/3/301/": task301.handler,
    "/tasks/3/302/": task302.handler,
    "/tasks/3/303/": task303.handler,
    "/tasks/3/304/": task304.handler,
    "/tasks/3/305/": task305.handler,
    "/tasks/3/306/": task306.handler,
    "/tasks/3/307/": task307.handler,
    "/tasks/3/309/": task309.handler,
    "/tasks/3/310/": task310.handler,
    "/tasks/3/311/": task311.handler,
    "/tasks/4/402/": task402.handler,
}


def get_handler(request: RequestT) -> HandlerT:
    handler = urlpatterns.get(request.path, handle_404)

    return handler
