# Generated by Django 3.2.16 on 2023-04-15 14:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apirestcrud', '0005_auto_20230415_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='day_income',
            field=models.DateTimeField(verbose_name=datetime.date(2023, 4, 15)),
        ),
    ]