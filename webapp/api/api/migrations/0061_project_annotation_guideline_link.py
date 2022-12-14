# Generated by Django 2.2.24 on 2021-11-02 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_auto_20211022_0940'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='annotation_guideline_link',
            field=models.TextField(blank=True, default='', help_text='link to an external document (i.e. GoogleDoc, MS Sharepoint)outlininng a guide for annotators to follow for this project,an example is available here: https://docs.google.com/document/d/1xxelBOYbyVzJ7vLlztP2q1Kw9F5Vr1pRwblgrXPS7QM/edit?usp=sharing'),
        ),
    ]
