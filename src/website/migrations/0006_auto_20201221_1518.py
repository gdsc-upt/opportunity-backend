# Generated by Django 3.1.4 on 2020-12-21 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_auto_20201221_1510"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menuitem",
            name="order_index",
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
    ]
