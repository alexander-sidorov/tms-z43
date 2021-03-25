from typing import Dict


def get_accumulated(session: Dict) -> int:
    result = session.get("task402", 0)

    return result


def add_number(session: Dict, number: int) -> int:
    acc = get_accumulated(session)
    acc += number
    session["task402"] = acc

    return number
