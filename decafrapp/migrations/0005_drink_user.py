# Generated by Django 3.1.1 on 2020-09-22 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('decafrapp', '0004_remove_drink_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]