# Generated by Django 4.0.3 on 2022-03-30 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companyprofile',
            options={'managed': True, 'verbose_name': 'CompanyProfile', 'verbose_name_plural': 'CompanyProfile'},
        ),
        migrations.AlterModelOptions(
            name='talktous',
            options={'managed': True, 'verbose_name': 'TalkToUs', 'verbose_name_plural': 'TalkToUs'},
        ),
        migrations.AlterModelTable(
            name='companyprofile',
            table='companyprofile',
        ),
        migrations.AlterModelTable(
            name='talktous',
            table='talktous',
        ),
    ]
