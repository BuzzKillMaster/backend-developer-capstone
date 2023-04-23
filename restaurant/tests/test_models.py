from django.test import TestCase

from restaurant.models import Menu

class MenuTestCase(TestCase):
    def test_get_menu(self):
        menu = Menu.objects.create(title="Pizza", price=10, inventory=10)
        self.assertEqual(menu.__str__(), "Pizza: 10")
