# Generated by Django 4.0.2 on 2022-07-24 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_petphoto_photo_alter_profile_gender'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]