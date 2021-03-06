# Generated by Django 3.1.4 on 2021-07-11 19:03

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
            name='Check_in_out_db_register',
            fields=[
                ('entry_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('attendance_date', models.DateField(auto_now=True)),
                ('day_off', models.BooleanField(default=False)),
                ('in_time', models.DateTimeField(null=True)),
                ('out_time', models.DateTimeField(null=True)),
                ('status', models.CharField(default='Not Arrived', max_length=200)),
                ('raised_absent', models.BooleanField(default=False)),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
