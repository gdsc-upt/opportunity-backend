# Generated by Django 3.1.5 on 2021-02-02 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("administration", "0003_auto_20210130_1945"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_email_confirmed",
            field=models.BooleanField(default=False, verbose_name="email confirmed"),
            preserve_default=False,
        ),
    ]
