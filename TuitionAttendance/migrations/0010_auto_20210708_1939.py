# Generated by Django 3.1.4 on 2021-07-08 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionAttendance', '0009_auto_20210708_1933'),
    ]

    operations = [
        migrations.RenameField(
            model_name='check_in_out_register',
            old_name='half_day',
            new_name='day_off',
        ),
    ]