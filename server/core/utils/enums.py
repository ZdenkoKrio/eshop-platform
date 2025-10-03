from __future__ import annotations
from enum import Enum


class StrEnum(str, Enum):
    def __str__(self) -> str:  # užitočné pre choices a serializáciu
        return str(self.value)

def to_django_choices(enum_cls: type[Enum]) -> list[tuple[str, str]]:
    return [(e.value, e.name.title().replace("_", " ")) for e in enum_cls]


class OrderStatus(StrEnum):
    DRAFT = "draft"
    UNPAID = "unpaid"
    PAID = "paid"
    SHIPPED = "shipped"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class PaymentStatus(StrEnum):
    NEW = "new"
    AUTHORIZED = "authorized"
    CAPTURED = "captured"
    FAILED = "failed"
    REFUNDED = "refunded"