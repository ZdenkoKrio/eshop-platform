from __future__ import annotations
from decimal import Decimal
from typing import NewType


CurrencyCode = NewType("CurrencyCode", str)  # napr. CurrencyCode("EUR")
PriceAmount = NewType("PriceAmount", Decimal)