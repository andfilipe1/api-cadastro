# Generated by Django 3.1 on 2020-08-13 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('M', 'Pessoa-Fisica'), ('V', 'Pessoa-Juridica'), ('N', 'Nao-Declarado')], default='V', max_length=1)),
                ('aluno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.cliente')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.produto')),
            ],
        ),
    ]
