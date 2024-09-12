# Generated by Django 5.1 on 2024-09-12 12:30

import django.core.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('select_type', models.CharField(choices=[('RELIG', 'Religião'), ('GENER', 'Gênero'), ('ORIEN', 'Orientação Sexual'), ('TRATA', 'Tratamento'), ('SINTO', 'Sintoma'), ('DOENC', 'Doença'), ('ALERG', 'Alergia'), ('MEDIC', 'Medicamento')], max_length=5)),
                ('value', models.CharField(max_length=256)),
                ('normalized_value', models.CharField(editable=False, max_length=256)),
                ('state', models.CharField(choices=[('ENA', 'enable'), ('DIS', 'disable'), ('TCK', 'tocheck')], default='TCK', max_length=3)),
            ],
            options={
                'permissions': [('can_create_with_any_state', 'Pode criar values com qualquer state'), ('can_create_only_with_tocheck_state', 'Pode criar somente values tocheck'), ('can_view_only_enableds_state', 'Pode visualizar apenas os valores validados'), ('can_view_all_states', 'Pode visualizar values com qualquer valor de state')],
            },
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128)),
                ('pseudonimo', models.CharField(max_length=128)),
                ('data_nascimento', models.DateField()),
                ('ja_fez_psicoterapia', models.BooleanField()),
                ('ja_fez_psiquiatrico', models.BooleanField()),
                ('ja_fez_tratamento_espirita', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('alergias', models.ManyToManyField(blank=True, limit_choices_to={'select_type': 'ALERG'}, related_name='none+', to='api.selectvalue')),
                ('genero', models.ManyToManyField(blank=True, limit_choices_to={'select_type': 'GENER'}, related_name='none+', to='api.selectvalue')),
                ('orientacao_sexual', models.ManyToManyField(blank=True, limit_choices_to={'select_type': 'ORIEN'}, related_name='none+', to='api.selectvalue')),
                ('religiao', models.ManyToManyField(blank=True, limit_choices_to={'select_type': 'RELIG'}, related_name='none+', to='api.selectvalue')),
            ],
            options={
                'permissions': [('can_view_realname_and_pseudonym', 'Permite ver ')],
            },
        ),
        migrations.CreateModel(
            name='NumeroDeTelefone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotulo', models.CharField(max_length=16)),
                ('ddd', models.CharField(max_length=15)),
                ('telefone', models.CharField(max_length=16)),
                ('whatsapp', models.BooleanField()),
                ('telegram', models.BooleanField()),
                ('ligacao', models.BooleanField()),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8, validators=[django.core.validators.MinLengthValidator(8)])),
                ('estado', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=64)),
                ('bairro', models.CharField(max_length=100)),
                ('tipo_logradouro', models.CharField(choices=[('NDA', 'Não se aplica'), ('OUT', 'Outro'), ('RUA', 'Rua'), ('AV', 'Avenida'), ('TRA', 'Travessa'), ('ROD', 'Rodovia'), ('AL', 'Alameda'), ('PRA', 'Praça'), ('EST', 'Estrada'), ('VL', 'Vila'), ('LRG', 'Largo'), ('BC', 'Beco'), ('QD', 'Quadra'), ('CON', 'Condomínio'), ('ST', 'Sítio'), ('FZ', 'Fazenda'), ('LT', 'Loteamento'), ('VL', 'Viela'), ('PQ', 'Parque')], default='NDA', max_length=4)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=5)),
                ('complemento', models.CharField(max_length=100)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=256)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitacaoAtendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('sintomas', models.ManyToManyField(blank=True, limit_choices_to={'select_type': 'SINTO'}, related_name='none+', to='api.selectvalue')),
                ('tratamentos_em_andamento', models.ManyToManyField(blank=True, limit_choices_to={'select_type': 'GENRO'}, related_name='none+', to='api.selectvalue')),
            ],
        ),
    ]
