# Generated by Django 3.1.4 on 2020-12-16 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_auto_20201216_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
