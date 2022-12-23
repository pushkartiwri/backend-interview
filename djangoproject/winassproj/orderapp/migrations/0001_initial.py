# Generated by Django 4.1.4 on 2022-12-22 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('totalfee', models.IntegerField()),
                ('serv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orderapp.services')),
            ],
        ),
    ]