# Generated by Django 3.1.4 on 2021-07-08 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionAttendance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='status',
            field=models.CharField(default='Not Arrived', max_length=200),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='in_time',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='out_time',
            field=models.DateTimeField(default=None),
        ),
    ]