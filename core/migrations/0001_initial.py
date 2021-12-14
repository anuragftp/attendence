# Generated by Django 3.2.3 on 2021-12-14 12:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.functions.datetime


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AnnualLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('month', models.DateTimeField(verbose_name=django.db.models.functions.datetime.ExtractMonth('start_date'))),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(blank=True, choices=[('SL', 'Sick-Leave'), ('ML', 'Maternity Leave')], max_length=100, null=True)),
                ('state', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Reject', 'Reject')], max_length=50, null=True)),
                ('reason', models.CharField(max_length=200)),
                ('maxleave', models.IntegerField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('update_on', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.TimeField(auto_now_add=True)),
                ('check_out', models.TimeField(auto_now=True)),
                ('working_hours', models.FloatField()),
                ('date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
