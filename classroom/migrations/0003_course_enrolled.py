# Generated by Django 3.2.10 on 2021-12-11 07:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('classroom', '0002_category_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrolled',
            field=models.ManyToManyField(related_name='course_owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
