# Generated by Django 3.1 on 2020-08-14 00:12

import cpf_field.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_fornecedor_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='nome',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cpf',
            field=cpf_field.models.CPFField(max_length=14, verbose_name='cpf'),
        ),
    ]
