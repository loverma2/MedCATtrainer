# Generated by Django 2.2.18 on 2021-03-12 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0053_remove_projectannotateentities_clinical_coding_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='concept',
            name='vocab',
        ),
    ]
