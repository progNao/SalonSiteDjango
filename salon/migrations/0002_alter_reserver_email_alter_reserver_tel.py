# Generated by Django 4.2 on 2024-02-15 21:22

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserver',
            name='email',
            field=models.EmailField(max_length=255),
        ),
        migrations.AlterField(
            model_name='reserver',
            name='tel',
            field=phone_field.models.PhoneField(max_length=255),
        ),
    ]
