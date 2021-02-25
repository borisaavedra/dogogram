# Generated by Django 3.1.6 on 2021-02-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profilefriend'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='profilefriend',
            constraint=models.UniqueConstraint(fields=('user_id', 'following_user_id'), name='unique_followers'),
        ),
    ]