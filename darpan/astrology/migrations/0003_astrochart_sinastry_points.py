# Generated by Django 2.1.4 on 2019-04-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrology', '0002_astrochart_chart'),
    ]

    operations = [
        migrations.AddField(
            model_name='astrochart',
            name='sinastry_points',
            field=models.CharField(blank=True, max_length=6000, null=True),
        ),
    ]
