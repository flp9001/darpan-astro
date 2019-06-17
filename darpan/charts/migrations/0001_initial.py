# Generated by Django 2.1.4 on 2019-03-14 20:41

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion
import timezone_field.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=255, verbose_name='full name')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique_with=('owner',))),
                ('date', models.DateField(blank=True, null=True)),
                ('time', models.TimeField(blank=True, null=True)),
                ('timezone', timezone_field.fields.TimeZoneField(blank=True)),
                ('datetime_utc', models.DateTimeField(blank=True, null=True)),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities.City')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cities.Country')),
            ],
        ),
    ]
