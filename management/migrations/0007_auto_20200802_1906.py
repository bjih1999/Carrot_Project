# Generated by Django 2.2.12 on 2020-08-02 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0006_auto_20200802_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrot',
            name='end_status',
            field=models.BooleanField(default=False),
        ),
    ]