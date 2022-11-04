from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

CITY = ((1, 'Rivne'),)


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

    body_type = models.ForeignKey(
        'BodyType',
        on_delete=models.CASCADE,
        related_name='cars'
    )
    mark = models.ForeignKey(
        'Mark',
        on_delete=models.CASCADE,
        related_name='cars',

    )
    renge_mileage = models.ForeignKey(
        'Mileage',
        on_delete=models.CASCADE,
        related_name='cars',

    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='cars',
        null=True,
        blank=True,
    )
    transmission = models.ForeignKey(
        'Transmission',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    year = models.ForeignKey(
        'Year',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    color = models.ForeignKey(
        'Color',
        on_delete=models.CASCADE,
        related_name='cars',
    )
    drivetrain = models.ForeignKey(
        'Drivetrain',
        on_delete=models.CASCADE,
        related_name='cars',
    )


class BodyType(models.Model):
    title = models.CharField(max_length=30)

    def count_this_body_type_car(self):
        count = self.objects.select_related('cars').get().cars.count()
        return count


class Mark(models.Model):
    title = models.CharField(max_length=30)

    def count_this_mark_car(self):
        count = self.objects.select_related('cars').get().cars.count()
        return count


class Mileage(models.Model):
    mileage_from = models.IntegerField()
    mileage_to = models.IntegerField()

    def count_this_mileage_car(self):
        count = self.objects.select_related('cars').get().cars.count()
        return count


class Transmission(models.Model):
    title = models.CharField(max_length=30)

    def count_this_transmission_car(self):
        count = self.objects.select_related('cars').get().cars.count()
        return count


class Year(models.Model):
    year = models.IntegerField()

    def count_this_year_car(self):
        count = self.objects.select_related('cars').get().cars.count()
        return count


class Drivetrain(models.Model):
    title = models.CharField(max_length=30)

    def count_this_drivetrain_car(self):
        count = self.objects.select_related('cars').get().cars.count()
        return count


class Color(models.Model):
    title = models.CharField(max_length=30)

    def count_this_color_car(self):
        count = self.objects.select_related('cars').get().cars.count()
        return count
