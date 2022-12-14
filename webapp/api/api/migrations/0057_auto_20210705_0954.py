# Generated by Django 2.2.24 on 2021-07-05 09:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0056_auto_20210417_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=300, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntityRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('validated', models.BooleanField(default=False)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entity_relation_document', to='api.Document')),
                ('end_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_entity', to='api.AnnotatedEntity')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Project')),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Relation')),
                ('start_entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_entity', to='api.AnnotatedEntity')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='projectannotateentities',
            name='relations',
            field=models.ManyToManyField(blank=True, default=None, help_text='Relations that will be available for this project', to='api.Relation'),
        ),
    ]
