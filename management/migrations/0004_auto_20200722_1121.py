# Generated by Django 2.2.14 on 2020-07-22 02:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20200722_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrot_test',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
