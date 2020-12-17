# Generated by Django 3.1.4 on 2020-12-17 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0005_auto_20201216_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=200)),
                ('orderedItem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.plant')),
                ('sellerId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.user')),
            ],
        ),
    ]