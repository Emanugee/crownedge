# Generated by Django 4.0.3 on 2022-04-27 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pix',
            field=models.ImageField(blank=True, default='profile/avatar.jpg', null=True, upload_to='profile'),
        ),
    ]
