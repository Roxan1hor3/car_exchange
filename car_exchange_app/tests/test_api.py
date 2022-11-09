from django.urls import reverse
from rest_framework.test import APITestCase

from car_exchange_app.models import Car


class CarsApiTestCase(APITestCase):
    def test_get(self):
        url = reverse('cars')
        print(url)
        responce = self.client.get(url)
        print(self.client)
        print(responce.data)
