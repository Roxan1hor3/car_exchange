# Generated by Django 4.1.3 on 2022-11-16 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_exchange_app', '0004_answer_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='tag',
        ),
    ]