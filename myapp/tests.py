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
        