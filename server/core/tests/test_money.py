from decimal import Decimal
from django.test import SimpleTestCase

from core.utils.money import Money, apply_discount, compute_vat


class MoneyUtilsTests(SimpleTestCase):
    def test_money_basic_arithmetics(self):
        a = Money(Decimal("10.00"), "EUR")
        b = Money(Decimal("2.00"), "EUR")
        self.assertEqual((a + b).amount, Decimal("12.00"))
        self.assertEqual((a - b).amount, Decimal("8.00"))
        self.assertEqual(a.mul(2).amount, Decimal("20.00"))

    def test_apply_discount_percent_and_abs(self):
        sub = Money(Decimal("100.00"), "EUR")
        disc, total = apply_discount(sub, discount_pct=10, discount_abs=Money(Decimal("5.00"), "EUR"))
        self.assertEqual(disc.amount, Decimal("15.00"))
        self.assertEqual(total.amount, Decimal("85.00"))

    def test_compute_vat(self):
        net = Money(Decimal("100.00"), "EUR")
        vat, gross = compute_vat(net, 21)
        self.assertEqual(vat.amount, Decimal("21.00"))
        self.assertEqual(gross.amount, Decimal("121.00"))