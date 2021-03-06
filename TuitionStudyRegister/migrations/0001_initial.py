# Generated by Django 3.1.4 on 2021-07-12 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyRegister',
            fields=[
                ('entry_id', models.AutoField(primary_key=True, serialize=False)),
                ('study_date', models.DateField(auto_now=True)),
                ('subject', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('study_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, max_length=200)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
