# Generated by Django 3.2.22 on 2023-10-18 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=' ', max_length=25)),
                ('Rollno', models.IntegerField(default=' ')),
                ('Date', models.DateField(default=' ')),
            ],
            options={
                'db_table': 'stud_attendance',
            },
        ),
        migrations.CreateModel(
            name='userregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default=' ', max_length=20)),
                ('Rollno', models.IntegerField(default=' ')),
                ('Username', models.CharField(default=' ', max_length=20)),
                ('Password', models.IntegerField(default=' ')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]