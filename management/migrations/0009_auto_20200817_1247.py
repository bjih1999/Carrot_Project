# Generated by Django 2.2.14 on 2020-08-17 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0008_remove_carrot_hp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrot',
            name='end_status',
            field=models.IntegerField(default=0),
        ),
    ]
