# Generated by Django 4.2.7 on 2023-11-30 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razao_social', models.CharField(max_length=100)),
                ('nome_fantasia', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=14, verbose_name='CNPJ')),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
    ]
