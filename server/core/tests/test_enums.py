from django.test import SimpleTestCase
from core.utils.enums import OrderStatus, to_django_choices


class EnumsUtilsTests(SimpleTestCase):
    def test_to_django_choices_contains_expected_values(self):
        choices = to_django_choices(OrderStatus)
        self.assertIn(("draft", "Draft"), choices)
        self.assertIn(("paid", "Paid"), choices)