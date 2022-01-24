# Generated by Django 4.0.1 on 2022-01-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('firstName', models.CharField(max_length=254)),
                ('lastName', models.CharField(max_length=254)),
                ('address', models.CharField(max_length=254)),
                ('postalCode', models.CharField(max_length=254)),
                ('dateOfBirth', models.DateField()),
                ('healthCardNum', models.CharField(max_length=254)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]