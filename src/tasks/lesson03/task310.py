import decimal
from typing import Dict
from typing import Tuple

from main.custom_types import RequestT
from main.custom_types import ResponseT
from main.util import render_template

TEMPLATE = "tasks/lesson03/task310.html"

BANKNOTE_ENDINGS = {
    range(0, 1): "ей",
    range(1, 2): "ь",
    range(2, 5): "я",
    range(5, 20): "ей",
}
BANKNOTE_SIGN = "\N{BANKNOTE WITH DOLLAR SIGN}"
BANKNOTE_STEM = "рубл"

COIN_ENDINGS = {
    range(0, 1): "ек",
    range(1, 2): "йка",
    range(2, 5): "йки",
    range(5, 20): "ек",
}
COIN_SIGN = "\N{FIRST PLACE MEDAL}"
COIN_STEM = "копе"

COINAGE: Dict[int, Tuple[str, str]]  # populated near the EOF
NO_MONEY = "\N{EMPTY SET}"


def handler(request: RequestT) -> ResponseT:
    money_raw = request.query.get("money", [""])[0]
    money = parse_decimal(money_raw)

    result1 = solution1(money)
    result2 = solution2(money)

    context = {
        "money": money_raw,
        "result1": result1,
        "result2": result2,
    }

    document = render_template(TEMPLATE, context)

    response = ResponseT(payload=document)

    return response


def solution1(money: decimal.Decimal) -> str:
    banknotes = money.to_integral_value(decimal.ROUND_FLOOR)
    coins = (abs(money - banknotes) * 100).to_integral_value(decimal.ROUND_FLOOR)

    rs = next(e for r, e in BANKNOTE_ENDINGS.items() if (banknotes % 20) in r)
    cs = next(e for r, e in COIN_ENDINGS.items() if (coins % 20) in r)

    rt = f"{banknotes} {BANKNOTE_STEM}{rs}" if banknotes else ""
    ct = f"{coins} {COIN_STEM}{cs}" if coins else ""

    result = ", ".join(t for t in (rt, ct) if t)
    if not result:
        result = NO_MONEY

    return result


def solution2(money: decimal.Decimal) -> str:
    money = int(money.fma(100, 0).to_integral_value(decimal.ROUND_FLOOR))

    items = []

    while money:
        for nominal, (name, medium) in reversed(sorted(COINAGE.items())):
            amount, money = divmod(money, nominal)
            if amount:
                items.append(f"{name} {medium} &times; {amount}")

    result = "\n".join(items)
    return result


def parse_decimal(value: str) -> decimal.Decimal:
    if not value:
        value = "0"

    value = value.replace(" ", "").replace(",", ".")
    result = decimal.Decimal(value)
    return result


COINAGE = {
    1: (solution1(decimal.Decimal("0.01")), COIN_SIGN),
    2: (solution1(decimal.Decimal("0.02")), COIN_SIGN),
    5: (solution1(decimal.Decimal("0.05")), COIN_SIGN),
    10: (solution1(decimal.Decimal("0.10")), COIN_SIGN),
    20: (solution1(decimal.Decimal("0.20")), COIN_SIGN),
    50: (solution1(decimal.Decimal("0.50")), COIN_SIGN),
    100: (solution1(decimal.Decimal("1")), COIN_SIGN),
    200: (solution1(decimal.Decimal("2")), COIN_SIGN),
    500: (solution1(decimal.Decimal("5")), BANKNOTE_SIGN),
    1000: (solution1(decimal.Decimal("10")), BANKNOTE_SIGN),
    2000: (solution1(decimal.Decimal("20")), BANKNOTE_SIGN),
    5000: (solution1(decimal.Decimal("50")), BANKNOTE_SIGN),
    10000: (solution1(decimal.Decimal("100")), BANKNOTE_SIGN),
    20000: (solution1(decimal.Decimal("200")), BANKNOTE_SIGN),
    50000: (solution1(decimal.Decimal("500")), BANKNOTE_SIGN),
}
