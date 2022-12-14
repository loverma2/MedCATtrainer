# Generated by Django 2.2.18 on 2021-02-16 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_auto_20210211_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='cuis_file',
            field=models.FileField(blank=True, help_text='A file containing a JSON formatted list of CUI code strings, i.e. ["1234567","7654321"]', null=True, upload_to=''),
        ),
    ]
