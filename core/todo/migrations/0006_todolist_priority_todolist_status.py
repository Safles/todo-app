# Generated by Django 5.0.6 on 2024-06-23 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_delete_tasklist'),
    ]

    operations = [
        migrations.AddField(
            model_name='todolist',
            name='priority',
            field=models.CharField(max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]