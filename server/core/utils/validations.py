from __future__ import annotations
from decimal import Decimal, InvalidOperation


def is_iso_currency(code: str) -> bool:
    return len(code) == 3 and code.isalpha() and code.isupper()


def parse_decimal_safe(value: str) -> Decimal:
    try:
        from decimal import Decimal
        return Decimal(value)
    
    except (InvalidOperation, ValueError) as e:
        raise ValueError(f"Invalid decimal: {value}") from e