from typing import TypeVar

from pydantic import BaseModel
from pydantic import validator


class CoefficientsT(BaseModel):
    a: complex = 0.0j
    b: complex = 0.0j
    c: complex = 0.0j

    @validator("*", pre=True)
    def validate_complex_values(cls, v):
        if isinstance(v, str):
            if not v:
                return 0j
            v = complex(v.replace(" ", ""))
        elif isinstance(v, (int, float)):
            v = v + 0j
        return v

    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True


AlgebraicNumberT = TypeVar("AlgebraicNumberT", complex, float, int)


def solution(
    coefficients: CoefficientsT,
    can_into_complex: bool,
) -> str:
    if not can_into_complex:
        if any(
            isinstance(i[1], complex) and not zero(i[1].imag)
            for i in coefficients
        ):
            raise ValueError("complex coefficients are not allowed")

    a, b, c = [getattr(coefficients, i) for i in "abc"]

    d = discriminant(a, b, c)
    if not can_into_complex and (d.real < 0 or not zero(d.imag)):
        raise ValueError("complex roots are not wanted")

    d **= 0.5

    if not zero(a):
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
    else:
        if not zero(b):
            # `bx + c = 0` => `x1,x2 = x = -c/b`
            x1 = x2 = -c / b
        else:
            # `c = 0` => no solutions
            raise ValueError("degenerate equation")

    x1 = round_generic(x1)
    x2 = round_generic(x2)

    x1 = normalize(x1)
    x2 = normalize(x2)

    if not can_into_complex and any(isinstance(x, complex) for x in (x1, x2)):
        raise ValueError("end up with unwanted complex roots")

    result = f"{x1 = }\n{x2 = }"
    return result


def zero(number: AlgebraicNumberT) -> bool:
    epsilon = 1e-5

    if isinstance(number, complex):
        result = all(abs(x) <= epsilon for x in (number.real, number.imag))
    elif isinstance(number, float):
        result = abs(number) <= epsilon
    else:
        result = number != 0

    return result


def discriminant(
    a: AlgebraicNumberT, b: AlgebraicNumberT, c: AlgebraicNumberT
) -> complex:
    d = b ** 2 - 4 * a * c
    return d


def round_generic(
    number: AlgebraicNumberT, digits: int = 4
) -> AlgebraicNumberT:
    if isinstance(number, complex):
        a = round(number.real, digits)
        b = round(number.imag, digits)
        result = complex(a, b)
    elif isinstance(number, float):
        result = round(number, digits)
    else:
        result = number

    return result


def normalize(number: AlgebraicNumberT) -> AlgebraicNumberT:
    result = number

    if isinstance(number, complex) and zero(number.imag):
        result = number.real

    return result
