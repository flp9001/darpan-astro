# Generated by Django 2.1.4 on 2019-06-17 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hds', '0002_auto_20190617_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='center',
            name='gates',
            field=models.ManyToManyField(to='hds.Gate'),
        ),
        migrations.AddField(
            model_name='center',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='center',
            name='slug',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
