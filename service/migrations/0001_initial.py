# Generated by Django 4.0.3 on 2022-03-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('coast', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('coast', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
