# Generated by Django 3.2.6 on 2021-12-28 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_following'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='_profiles_profile_following_+', to='profiles.Profile'),
        ),
    ]
