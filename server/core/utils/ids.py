from __future__ import annotations
import secrets
import string


def short_token(length: int = 12) -> str:
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def human_order_number(prefix: str = "ORD") -> str:
    return f"{prefix}-{short_token(10)}".upper()