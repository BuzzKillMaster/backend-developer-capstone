from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json

class MenuViewTest(TestCase):
    def setUp(self) -> None:
        Menu.objects.create(title="Pizza", price=10, inventory=10)
        Menu.objects.create(title="Burger", price=10, inventory=10)
        Menu.objects.create(title="Pasta", price=10, inventory=10)

    def test_getall(self):
        client = Client()
        response = client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), serializer.data)