# Generated by Django 3.1.4 on 2020-12-20 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administration', '0003_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='WantToHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='OpportunityCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('slug', models.SlugField()),
                ('created', models.DateTimeField()),
                ('updated', models.DateTimeField()),
                ('opportunities', models.ManyToManyField(to='administration.Opportunity')),
            ],
        ),
    ]
