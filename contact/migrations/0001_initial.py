# Generated by Django 4.1.3 on 2022-12-03 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('PhoneNumber', models.CharField(max_length=11)),
                ('Email', models.EmailField(max_length=254)),
                ('Massege', models.TextField()),
            ],
        ),
    ]
