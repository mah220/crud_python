# Generated by Django 4.1.4 on 2022-12-10 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0006_veiculo_km'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motorista',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('telefone', models.CharField(max_length=100, verbose_name='Marca')),
                ('cnh', models.CharField(max_length=100, verbose_name='CNH')),
            ],
        ),
    ]
