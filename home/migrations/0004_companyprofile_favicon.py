# Generated by Django 4.0.3 on 2022-04-13 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_companyprofile_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyprofile',
            name='favicon',
            field=models.ImageField(blank=True, default='/favicon-96x96.png', null=True, upload_to='logo'),
        ),
    ]
