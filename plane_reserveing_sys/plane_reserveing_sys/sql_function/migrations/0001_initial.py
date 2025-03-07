# Generated by Django 5.1.1 on 2024-10-05 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Traveler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('work_unit', models.CharField(max_length=200)),
                ('id_number', models.CharField(max_length=20)),
                ('travel_date', models.DateField()),
                ('destination', models.CharField(max_length=200)),
                ('file', models.FileField(blank=True, null=True, upload_to='travel_files/')),
            ],
        ),
    ]
