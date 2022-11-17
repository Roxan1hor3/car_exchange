from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

CITY = (('Rivne', 'Rivne'), ('Kiyv', 'Kiyv'))


class Car(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    main_photo = models.ImageField(upload_to='media')
    other_photo = models.ImageField(upload_to='media', null=True, blank=True)
    city = models.CharField(max_length=50, choices=CITY)
    run = models.IntegerField()
    accidents = models.BooleanField(default=False)
    description_accidents = models.TextField(max_length=300)
    phone = PhoneNumberField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)

    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cars',
        null=True,
        blank=True,
    )
    category = models.ManyToManyField(
        'Category',
        related_name='cars',
    )


class Category(models.Model):
    title = models.CharField(max_length=50)


class SubCategory(models.Model):
    title = models.CharField(max_length=50)

    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='sub_category',
    )


class Answer(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    text_question = models.TextField(max_length=300)
    parent = models.ForeignKey(
        'self',
        verbose_name='answers',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='children',
    )

    question = models.ForeignKey(
        'Question',
        verbose_name='answers',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='answers',
    )

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='answers'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='answers'
    )


class Question(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    text_question = models.TextField(max_length=300)

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        related_name='questions'
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='questions'
    )


class Message(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    text_message = models.TextField(max_length=200)

    car = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
    )

    user = models.ManyToManyField(
        User
    )

    question = models.ForeignKey(
        Question,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    answer = models.ForeignKey(
        Answer,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )


class Wish(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
