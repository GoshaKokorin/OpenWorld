# Generated by Django 4.1.2 on 2022-10-24 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmailCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100, verbose_name='email')),
                ('code', models.CharField(max_length=100, verbose_name='code')),
            ],
        ),
    ]
