# Generated by Django 3.1.1 on 2020-09-22 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decafrapp', '0003_drink_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drink',
            name='user',
        ),
    ]