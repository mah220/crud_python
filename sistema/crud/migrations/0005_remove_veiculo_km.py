# Generated by Django 4.1.4 on 2022-12-09 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0004_veiculo_km'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='veiculo',
            name='km',
        ),
    ]
