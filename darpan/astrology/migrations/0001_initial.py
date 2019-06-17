# Generated by Django 2.1.4 on 2019-03-14 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AstroChart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sun', models.FloatField()),
                ('moon', models.FloatField()),
                ('mercury', models.FloatField()),
                ('venus', models.FloatField()),
                ('mars', models.FloatField()),
                ('jupiter', models.FloatField()),
                ('saturn', models.FloatField()),
                ('uranus', models.FloatField()),
                ('neptune', models.FloatField()),
                ('pluto', models.FloatField()),
            ],
        ),
    ]
