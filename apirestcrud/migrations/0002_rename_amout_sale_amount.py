# Generated by Django 3.2.16 on 2023-04-15 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apirestcrud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='amout',
            new_name='amount',
        ),
    ]
