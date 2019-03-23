# Generated by Django 2.1.7 on 2019-03-23 00:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(max_length=50)),
                ('idBairro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Bairro')),
            ],
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cnpj', models.CharField(max_length=14)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=11)),
                ('senha', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=11)),
                ('idPessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='TipoTelefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='telefone',
            name='idTipoTelefone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.TipoTelefone'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='idPessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Pessoa'),
        ),
    ]
