# Generated by Django 4.2.7 on 2023-11-30 02:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_descricao', models.CharField(max_length=100)),
                ('codigo_barra', models.CharField(max_length=100)),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField(default=0)),
                ('img_produto', models.ImageField(blank=True, null=True, upload_to='img_produto')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadeMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SaidaNfe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name=' Descrição da Saída')),
                ('quantidade', models.IntegerField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.produto')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='unidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.unidademedida'),
        ),
        migrations.CreateModel(
            name='Movimentacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('SAIDAS', 'SAIDAS'), ('ENTRADA', 'ENTRADAS')], max_length=15)),
                ('quantidade', models.IntegerField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('saldo', models.IntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.produto')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='EntradaNfe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name=' Descrição da Entrada')),
                ('numero_nfe', models.IntegerField()),
                ('quantidade', models.IntegerField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='logistics.produto')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]