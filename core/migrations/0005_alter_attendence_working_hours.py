# Generated by Django 3.2.3 on 2021-12-14 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_annualleave_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='working_hours',
            field=models.FloatField(default=0),
        ),
    ]