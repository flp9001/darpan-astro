# Generated by Django 2.1.4 on 2019-03-14 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('astrology', '0001_initial'),
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='astrochart',
            name='chart',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='astrochart', to='charts.Chart'),
        ),
    ]
