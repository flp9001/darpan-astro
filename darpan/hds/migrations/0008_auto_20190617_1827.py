# Generated by Django 2.1.4 on 2019-06-17 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hds', '0007_auto_20190617_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='gate',
            name='slug',
            field=models.SlugField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='center',
            name='slug',
            field=models.SlugField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
