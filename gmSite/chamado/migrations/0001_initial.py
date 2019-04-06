# Generated by Django 2.1.7 on 2019-04-02 16:03

import cadastros.models
import orgao.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPessoa', models.IntegerField(verbose_name=cadastros.models.Pessoa)),
                ('idEvento', models.IntegerField(verbose_name=orgao.models.Eventos)),
                ('idStatus', models.IntegerField(verbose_name="STATUS")),
                ('idEndereco', models.IntegerField(verbose_name=cadastros.models.Endereco)),
                ('dataAbertura', models.DateField(default=None, verbose_name='ABERTO EM')),
                ('dataFechamento', models.DateField(blank=True, default=None, null=True, verbose_name='CONCLUÍDO EM')),
                ('observacao', models.CharField(max_length=200, verbose_name='OBSERVAÇÃO')),
            ],
        ),
    ]
