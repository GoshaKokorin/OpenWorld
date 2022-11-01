# Generated by Django 4.1.2 on 2022-10-31 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetEmailCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=64, unique=True, verbose_name='email')),
                ('code', models.CharField(max_length=6, verbose_name='code')),
            ],
        ),
    ]
