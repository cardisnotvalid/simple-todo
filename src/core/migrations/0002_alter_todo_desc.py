# Generated by Django 5.0.4 on 2024-05-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='desc',
            field=models.TextField(blank=True, default='No description', null=True),
        ),
    ]
