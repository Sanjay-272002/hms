# Generated by Django 3.2.16 on 2022-10-31 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0003_auto_20221031_0854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bed_number', models.CharField(max_length=50)),
                ('occupied', models.BooleanField()),
            ],
        ),
    ]