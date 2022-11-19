from django.test import TestCase
from .forms import *
from django.contrib.auth.models import User
# Create your tests here.

class AnimalTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="pep", password="somepassword")

    def test_valid_paramsA(self):
        user = User.objects.get(name="pep")
        self.assertEqual(user.get_full_name(), "Somename")
    def test_valid_paramsB(self):
        user = User.objects.get(name="pep")
        self.assertEqual(user.check_password(), "equalpassword")
    def test_valid_paramsC(self):
        user = User.objects.get(name="pep")
        self.assertEqual(user.get_full_name(), "Someemail")
    def test_valid_paramsD(self):
        user = User.objects.get(name="pep")
        self.assertEqual(user.get_username, "pep")
    def test_valid_paramsE(self):
        user = User.objects.get(name="pep")
        self.assertEqual(user.get_group_permissions(), "normalUser")