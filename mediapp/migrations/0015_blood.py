# Generated by Django 3.0.5 on 2022-11-03 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediapp', '0014_bed_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='blood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40, null=True)),
                ('Phone', models.CharField(max_length=40, null=True)),
                ('Blood', models.TextField(max_length=10, null=True)),
                ('Address', models.TextField(max_length=80, null=True)),
            ],
        ),
    ]
