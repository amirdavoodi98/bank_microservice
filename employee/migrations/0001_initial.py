# Generated by Django 4.0.5 on 2022-06-07 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.branch')),
            ],
        ),
    ]
