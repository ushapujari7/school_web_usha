# Generated by Django 4.2 on 2025-02-23 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='experience',
            field=models.IntegerField(default=0),
        ),
    ]
