# Generated by Django 4.0.2 on 2022-07-23 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_pet_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petphoto',
            name='photo',
            field=models.ImageField(upload_to='pets/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=20, null=True),
        ),
    ]