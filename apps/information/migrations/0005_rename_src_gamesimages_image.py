# Generated by Django 4.1.2 on 2022-11-02 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0004_alter_video_options_remove_gamesimages_games_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gamesimages',
            old_name='src',
            new_name='image',
        ),
    ]
