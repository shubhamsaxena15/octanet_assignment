# Generated by Django 4.2.8 on 2024-01-29 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='category',
        ),
        migrations.RemoveField(
            model_name='task',
            name='label',
        ),
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(max_length=5),
        ),
    ]
