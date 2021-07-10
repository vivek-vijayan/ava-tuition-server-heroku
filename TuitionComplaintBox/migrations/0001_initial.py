# Generated by Django 3.1.4 on 2021-07-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('complaint_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('complaint_description', models.TextField(blank=True)),
                ('student_id', models.IntegerField(default=0)),
                ('student_name', models.CharField(blank=True, max_length=255)),
                ('raised_on', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(blank=True, max_length=255)),
                ('raised_by', models.IntegerField(default=0)),
            ],
        ),
    ]