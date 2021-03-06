# Generated by Django 3.2.9 on 2021-12-11 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualizer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='energy',
            name='generator_anual_net',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='plant_information',
            name='nameplate_capacity',
            field=models.DecimalField(blank=True, decimal_places=3, default=None, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='plant_information',
            name='num_boilers',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='plant_information',
            name='num_generator',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='plant_information',
            name='primary_fuel',
            field=models.CharField(blank=True, default=None, max_length=5, null=True),
        ),
    ]
