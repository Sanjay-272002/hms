# Generated by Django 3.0.5 on 2022-11-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0012_auto_20221101_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='oxygen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_num', models.PositiveIntegerField(null=True)),
            ],
        ),
    ]
