# Generated by Django 3.1.6 on 2021-02-23 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210223_2327'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='followingfollowers',
            name='unique_followers',
        ),
        migrations.RenameField(
            model_name='followingfollowers',
            old_name='following_user_id',
            new_name='follower_profile',
        ),
        migrations.RenameField(
            model_name='followingfollowers',
            old_name='user_id',
            new_name='following_profile',
        ),
        migrations.AddConstraint(
            model_name='followingfollowers',
            constraint=models.UniqueConstraint(fields=('following_profile', 'follower_profile'), name='unique_followers'),
        ),
    ]
