import glob
import json
import os

from django.contrib.auth.models import User
from rest_framework.test import APITestCase

from car_exchange_app.models import Category, SubCategory, Car, Question, Answer
from car_exchange_app.serializers import CarDetailSerializers
from car_exchange_app.tests.test_api import temporary_image, delete_test_file


class CarListSerializersTestCase(APITestCase):
    def setUp(self):
        self.category1 = Category.objects.create(title='category 2')
        self.category2 = Category.objects.create(title='category 3')

        self.subcategory1 = SubCategory.objects.create(title='subcategory 1', category=self.category1)
        self.subcategory2 = SubCategory.objects.create(title='subcategory 2', category=self.category1)
        self.subcategory3 = SubCategory.objects.create(title='subcategory 3', category=self.category2)
        self.subcategory4 = SubCategory.objects.create(title='subcategory 4', category=self.category2)

        self.user1 = User.objects.create(username='user1', password='123qwer')
        self.user2 = User.objects.create(username='user2', password='123qwer')

        self.car1 = Car.objects.create(name='car 5', description='qwerasdf',
                                       main_photo=temporary_image(),
                                       city='Rivne', run=123512, accidents=True, description_accidents='QEWRADSF',
                                       phone='+380988181628')
        self.car2 = Car.objects.create(name='car 6', description='qwerasdf',
                                       main_photo=temporary_image(),
                                       city='Kiev', run=123512, accidents=True, description_accidents='QEasdfWRADSF',
                                       phone='+380988181628')

        self.car1.category.add(self.category1, self.category2)
        self.car2.category.add(self.category2, self.category1)

        self.question1 = Question.objects.create(text_question='qwerasff', car=self.car1, user=self.user1)
        self.question2 = Question.objects.create(text_question='qwerasff', car=self.car2, user=self.user2)

        self.answer1 = Answer.objects.create(text_question='qwerasff', car=self.car1, user=self.user1,
                                             question=self.question1)
        self.answer2 = Answer.objects.create(text_question='qwerasff', car=self.car2, user=self.user2,
                                             question=self.question1)
        self.answer3 = Answer.objects.create(text_question='qwerasff', car=self.car1, user=self.user1,
                                             question=self.question2)
        self.answer4 = Answer.objects.create(text_question='qwerasff', car=self.car2, user=self.user2,
                                             question=self.question2)

        self.car1.seller = self.user1
        self.car2.seller = self.user2

    def test_detail_cart(self):
        data = CarDetailSerializers([self.car1, self.car2], many=True).data
        print(json.dumps(data, indent=4))
        expected_data = [
            {
                "id": 1,
                "questions": [
                    {
                        "id": 1,
                        "answers": [
                            {
                                "id": 1,
                                "created_at": self.answer1.created_at,
                                "updated_at": self.answer1.updated_at,
                                "text_question": "qwerasff",
                                "question": 1,
                                "car": 1
                            },
                            {
                                "id": 2,
                                "created_at": self.answer2.created_at,
                                "updated_at": self.answer2.updated_at,
                                "text_question": "qwerasff",
                                "question": 1,
                                "car": 2
                            }
                        ],
                        "created_at": self.question1.created_at,
                        "updated_at": self.question1.updated_at,
                        "text_question": "qwerasff",
                        "car": 1,
                        "user": 1
                    }
                ],
                "category": [
                    {
                        "id": 1,
                        "sub_category": [
                            {
                                "id": 1,
                                "title": "subcategory 1",
                                "category": 1
                            },
                            {
                                "id": 2,
                                "title": "subcategory 2",
                                "category": 1
                            }
                        ],
                        "title": "category 2"
                    },
                    {
                        "id": 2,
                        "sub_category": [
                            {
                                "id": 3,
                                "title": "subcategory 3",
                                "category": 2
                            },
                            {
                                "id": 4,
                                "title": "subcategory 4",
                                "category": 2
                            }
                        ],
                        "title": "category 3"
                    }
                ],
                "seller": "user1",
                "name": "car 5",
                "description": "qwerasdf",
                "main_photo": '/media/' + str(self.car1.main_photo),
                "other_photo": None,
                "city": "Rivne",
                "run": 123512,
                "accidents": True,
                "description_accidents": "QEWRADSF",
                "phone": "+380988181628",
                "created_at": self.car1.created_at,
                "updated_at": self.car1.updated_at
            },
            {
                "id": 2,
                "questions": [
                    {
                        "id": 2,
                        "answers": [
                            {
                                "id": 3,
                                "created_at": self.answer3.created_at,
                                "updated_at": self.answer3.updated_at,
                                "text_question": "qwerasff",
                                "question": 2,
                                "car": 1
                            },
                            {
                                "id": 4,
                                "created_at": self.answer4.created_at,
                                "updated_at": self.answer4.updated_at,
                                "text_question": "qwerasff",
                                "question": 2,
                                "car": 2
                            }
                        ],
                        "created_at": self.question2.created_at,
                        "updated_at": self.question2.updated_at,
                        "text_question": "qwerasff",
                        "car": 2,
                        "user": 2
                    }
                ],
                "category": [
                    {
                        "id": 1,
                        "sub_category": [
                            {
                                "id": 1,
                                "title": "subcategory 1",
                                "category": 1
                            },
                            {
                                "id": 2,
                                "title": "subcategory 2",
                                "category": 1
                            }
                        ],
                        "title": "category 2"
                    },
                    {
                        "id": 2,
                        "sub_category": [
                            {
                                "id": 3,
                                "title": "subcategory 3",
                                "category": 2
                            },
                            {
                                "id": 4,
                                "title": "subcategory 4",
                                "category": 2
                            }
                        ],
                        "title": "category 3"
                    }
                ],
                "seller": "user2",
                "name": "car 6",
                "description": "qwerasdf",
                "main_photo": '/media/' + str(self.car2.main_photo),
                "other_photo": None,
                "city": "Kiev",
                "run": 123512,
                "accidents": True,
                "description_accidents": "QEasdfWRADSF",
                "phone": "+380988181628",
                "created_at": self.car2.created_at,
                "updated_at": self.car2.updated_at
            }
        ]
        self.assertEqual(json.dumps(expected_data), json.dumps(data))
        delete_test_file()
