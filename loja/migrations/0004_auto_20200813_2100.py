# Generated by Django 3.1 on 2020-08-14 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_auto_20200813_2057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fornecedor',
            old_name='cnpj',
            new_name='CNPJ',
        ),
    ]