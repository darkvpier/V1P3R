# Generated by Django 3.1.4 on 2021-05-18 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('descript', models.CharField(max_length=255)),
                ('platform_name', models.CharField(max_length=255)),
                ('platform_mode', models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=10)),
                ('starting_date', models.DateField()),
                ('ending_date', models.DateField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='event_photo/')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='event_thumbnail/')),
            ],
        ),
    ]
