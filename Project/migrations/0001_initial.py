# Generated by Django 5.0.6 on 2024-07-07 19:56

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Technologies',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('project_link', models.TextField()),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('description', models.TextField()),
                ('role', models.CharField(choices=[('frontend', 'Frontend'), ('backend', 'Backend'), ('fullstack', 'Fullstack')], default='frontend', max_length=20)),
                ('image', models.ImageField(upload_to='project-banner-image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('technologies', models.ManyToManyField(to='Project.technology')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
