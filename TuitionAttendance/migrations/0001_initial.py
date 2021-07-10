# Generated by Django 3.1.4 on 2021-07-06 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.IntegerField(null=True)),
                ('attendance_date', models.DateField(auto_now=True)),
                ('half_day', models.BooleanField(default=False)),
                ('in_time', models.DateTimeField(auto_now=True)),
                ('out_time', models.DateTimeField(null=True)),
            ],
        ),
    ]