# Generated by Django 4.1.2 on 2022-11-03 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='communication',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
