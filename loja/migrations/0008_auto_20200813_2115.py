# Generated by Django 3.1 on 2020-08-14 00:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0007_remove_produto_nivel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fornecedor',
            name='cliente',
        ),
        migrations.AddField(
            model_name='produto',
            name='cliente',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='loja.cliente'),
            preserve_default=False,
        ),
    ]
