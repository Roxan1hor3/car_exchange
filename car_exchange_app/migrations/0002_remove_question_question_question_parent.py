# Generated by Django 4.1.3 on 2022-11-08 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('car_exchange_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question',
        ),
        migrations.AddField(
            model_name='question',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='car_exchange_app.question', verbose_name='Question'),
        ),
    ]