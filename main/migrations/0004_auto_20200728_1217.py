# Generated by Django 2.2.4 on 2020-07-28 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200728_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='amount',
            field=models.IntegerField(),
        ),
    ]