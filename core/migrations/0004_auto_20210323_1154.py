# Generated by Django 3.1.7 on 2021-03-23 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210322_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='tracker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tracker', to='core.habittracker'),
        ),
    ]
