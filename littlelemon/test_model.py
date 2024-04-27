from django.test import TestCase
from restaurant.models import Menu
from decimal import Decimal

class MenuTest(TestCase):

    def test_create_item(self):
        item = Menu.objects.create(Title="IceCream", Price=Decimal('80'), Inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

