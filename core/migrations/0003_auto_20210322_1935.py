# Generated by Django 3.1.7 on 2021-03-22 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210322_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='goal_type',
            field=models.CharField(max_length=100),
        ),
    ]
