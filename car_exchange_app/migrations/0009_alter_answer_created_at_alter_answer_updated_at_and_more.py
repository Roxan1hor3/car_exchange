# Generated by Django 4.1.3 on 2022-11-16 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_exchange_app', '0008_alter_message_created_at_alter_message_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='created_at',
            field=models.DateField(default='2022-11-16 14:47:30'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='updated_at',
            field=models.DateField(default='2022-11-16 14:47:30'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default='2022-11-16 14:47:30'),
        ),
        migrations.AlterField(
            model_name='message',
            name='updated_at',
            field=models.DateTimeField(default='2022-11-16 14:47:30'),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_at',
            field=models.DateField(default='2022-11-16 14:47:30'),
        ),
        migrations.AlterField(
            model_name='question',
            name='updated_at',
            field=models.DateField(default='2022-11-16 14:47:30'),
        ),
    ]