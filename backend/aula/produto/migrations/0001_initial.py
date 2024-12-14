# Generated by Django 5.1.4 on 2024-12-13 00:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantidade', models.PositiveIntegerField()),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('data_atualizacao', models.DateTimeField(auto_now=True)),
                ('estoque_minimo', models.PositiveIntegerField()),
                ('estoque_maximo', models.PositiveIntegerField()),
                ('disponivel', models.BooleanField(default=True)),
                ('em_promoção', models.BooleanField(default=False)),
                ('desconto', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('categoria', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='produto.categoria')),
            ],
        ),
    ]
