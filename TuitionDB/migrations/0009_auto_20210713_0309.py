# Generated by Django 3.1.4 on 2021-07-12 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TuitionDB', '0008_auto_20210712_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leader',
            name='leader_roles',
            field=models.CharField(choices=[('Administrator', 'Administrator'), ('Check-in Leader', 'Check-in Leader'), ('File Leader', 'File Leader'), ('Diary Leader', 'Diary Leader')], max_length=200),
        ),
    ]
