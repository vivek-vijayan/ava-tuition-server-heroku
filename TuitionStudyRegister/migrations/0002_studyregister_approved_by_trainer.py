# Generated by Django 3.1.4 on 2021-07-17 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionStudyRegister', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyregister',
            name='approved_by_trainer',
            field=models.BooleanField(default=False),
        ),
    ]