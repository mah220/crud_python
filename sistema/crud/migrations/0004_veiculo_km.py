# Generated by Django 4.1.4 on 2022-12-09 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_remove_veiculo_km'),
    ]

    operations = [
        migrations.AddField(
            model_name='veiculo',
            name='km',
            field=models.CharField(default=20, max_length=100, verbose_name='Km_Troca_Óleo'),
            preserve_default=False,
        ),
    ]