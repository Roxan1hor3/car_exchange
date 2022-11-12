import os
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from setuptools import glob

from car_exchange_app.models import Car, Category, Question, Answer, SubCategory
from car_exchange_app.serializers import CarListSerializers


def temporary_image():
    bts = BytesIO()
    img = Image.new("RGB", (100, 100))
    img.save(bts, 'jpeg')
    return SimpleUploadedFile("test.jpg", bts.getvalue())


def delete_test_file():
    fileList = glob.glob('media/media/test_*.jpg', recursive=True)

    # Remove all files one by one
    for file in fileList:
        try:
            os.remove(file)
        except OSError:
            print("Error while deleting file")


class CarsApiTestCase(APITestCase):
    def test_get(self):
        category1 = Category.objects.create(title='category 2')
        category2 = Category.objects.create(title='category 3')

        subcategory1 = SubCategory.objects.create(title='subcategory 1', category=category1)
        subcategory2 = SubCategory.objects.create(title='subcategory 2', category=category1)
        subcategory3 = SubCategory.objects.create(title='subcategory 3', category=category2)
        subcategory4 = SubCategory.objects.create(title='subcategory 4', category=category2)

        user1 = User.objects.create(username='user1', password='123qwer')
        user2 = User.objects.create(username='user2', password='123qwer')

        car1 = Car.objects.create(name='car 5', description='qwerasdf',
                                  main_photo=temporary_image(),
                                  city='Rivne', run=123512, accidents=True, description_accidents='QEWRADSF',
                                  phone='+380988181628')
        car2 = Car.objects.create(name='car 6', description='qwerasdf',
                                  main_photo=temporary_image(),
                                  city='Kiev', run=123512, accidents=True, description_accidents='QEasdfWRADSF',
                                  phone='+380988181628')

        car1.category.add(category1, category2)
        car2.category.add(category2, category1)

        question1 = Question.objects.create(text_question='qwerasff', car=car1, user=user1)
        question2 = Question.objects.create(text_question='qwerasff', car=car2, user=user2)

        answer1 = Answer.objects.create(text_question='qwerasff', car=car1, user=user1, question=question1)
        answer2 = Answer.objects.create(text_question='qwerasff', car=car2, user=user2, question=question1)
        answer3 = Answer.objects.create(text_question='qwerasff', car=car1, user=user1, question=question2)
        answer4 = Answer.objects.create(text_question='qwerasff', car=car2, user=user2, question=question2)

        car1.seller = user1
        car2.seller = user2

        url = reverse('cars')
        response = self.client.get(url)
        serializer_data = CarListSerializers([car1, car2], many=True).data

        self.assertEqual(status.HTTP_200_OK, response.status_code)
        """ Response creates a test server for the photo and assert is not confirmed 
        because the prefix http://testserver is added to the relative path to the photo
        the following code checks for the presence of a relative path in example
        http://testserver/media/media/test_0Vwcrxn.jpg """
        if serializer_data[0]['main_photo'] in response.data[0]['main_photo']:
            response.data[0]['main_photo'] = serializer_data[0]['main_photo']
        if serializer_data[1]['main_photo'] in response.data[1]['main_photo']:
            response.data[1]['main_photo'] = serializer_data[1]['main_photo']

        self.assertEqual(serializer_data, response.data)
        delete_test_file()
