# Generated by Django 3.1.3 on 2020-11-13 16:56

import api.utils
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sound',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('text_content', models.TextField(blank=True, null=True)),
                ('audio_join', models.FileField(blank=True, null=True, upload_to=api.utils.get_path_media)),
                ('audio_join_Transformed', models.FileField(blank=True, null=True, upload_to=api.utils.get_path_media_audio_transformation)),
                ('converted', models.BooleanField(default=False)),
                ('inference_time', models.CharField(blank=True, max_length=255, null=True)),
                ('inference_time_model_parametre_execution', models.CharField(blank=True, max_length=255, null=True)),
                ('inference_time_audio_saving', models.CharField(blank=True, max_length=255, null=True)),
                ('is_tts', models.BooleanField(default=False)),
                ('is_male', models.BooleanField(default=False)),
                ('verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Sound',
                'verbose_name_plural': 'Sounds',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('text_content', models.TextField(blank=True, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'TextContent',
                'verbose_name_plural': 'TextContents',
            },
        ),
    ]
