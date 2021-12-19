# Generated by Django 3.2.9 on 2021-12-16 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0008_auto_20211211_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='energy',
            name='plant',
        ),
        migrations.AddField(
            model_name='energy',
            name='plant_information',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='visualizer.plant_information'),
            preserve_default=False,
        ),
    ]