import random
from django.test import TestCase
from .forms import *
from django.contrib.auth.models import User
from .models import *
# Create your tests here.

class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="pep", password="somepassword")

    def test_valid_info(self):
        platos = PlatoComida.objects.all()
        for plato in platos:
            self.assertEqual(plato.name, "test")
            self.assertEqual(plato.price, "test")
            self.assertEqual(plato.description, "test")
            self.assertEqual(plato.image, "test")
            
    def test_buy_cart(self):
        data = "some data"
        carts = CarritoCompra.objects.all()
        for cart in carts:
            self.assertEqual(cart.name, "test")
            self.assertEqual(cart.price, "test")
            self.assertEqual(cart.description, "test")
            self.assertEqual(cart.image, "test")
        query = CarritoCompra(user=None)
        query.cart = [ elem.name for elem in PlatoComida.objects.all()]
        query.cart = ""
        for q in query.cart:
            query.cart += str(q) + "-" + str(random.Random.randint()) + r"/"
        self.assertAlmostEquals(data)
        