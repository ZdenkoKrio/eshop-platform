from __future__ import annotations
from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP, getcontext

# Bezpečné zaokrúhľovanie na 2 desatinné miesta pre meny
getcontext().prec = 28


@dataclass(frozen=True, slots=True)
class Money:
    amount: Decimal
    currency: str  # "EUR", "CZK", "USD"

    def quantize(self) -> "Money":
        return Money(self.amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), self.currency)

    # Základné operácie — vyhodia ValueError ak miešaš meny
    def _check_currency(self, other: "Money") -> None:
        if self.currency != other.currency:
            raise ValueError(f"Currency mismatch: {self.currency} != {other.currency}")

    def __add__(self, other: "Money") -> "Money":
        self._check_currency(other)
        return Money(self.amount + other.amount, self.currency).quantize()

    def __sub__(self, other: "Money") -> "Money":
        self._check_currency(other)
        return Money(self.amount - other.amount, self.currency).quantize()

    def mul(self, k: int | Decimal | float) -> "Money":
        d = Decimal(str(k))
        return Money((self.amount * d), self.currency).quantize()

    def is_negative(self) -> bool:
        return self.amount < 0


def percent(value: Money, pct: Decimal | float | int) -> Money:
    d = Decimal(str(pct)) / Decimal("100")
    return value.mul(d)


def apply_discount(subtotal: Money, discount_pct: Decimal | float | int | None = None,
                   discount_abs: Money | None = None) -> tuple[Money, Money]:
    """
    Vráti (discount_total, total_after_discount). Negatívne výsledky ošetri na nulu.
    """
    discount = Money(Decimal("0"), subtotal.currency)
    if discount_pct:
        discount = discount + percent(subtotal, discount_pct)
    if discount_abs:
        discount._check_currency(subtotal)
        discount = discount + discount_abs
    total = subtotal - discount
    if total.is_negative():
        total = Money(Decimal("0"), subtotal.currency)
        discount = subtotal
    return (discount.quantize(), total.quantize())


def compute_vat(net: Money, vat_rate_pct: Decimal | float | int) -> tuple[Money, Money]:
    """Z net sumy vyrátaj VAT a gross (net + VAT)."""
    vat = percent(net, vat_rate_pct)
    return (vat.quantize(), (net + vat).quantize())