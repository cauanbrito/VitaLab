# Generated by Django 5.0.3 on 2024-03-25 22:44

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exames', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SolicitacaoExame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('E', 'Em análise'), ('F', 'Finalizado')], max_length=2)),
                ('resultado', models.FileField(blank=True, null=True, upload_to='resultados')),
                ('requer_senha', models.BooleanField(default=False)),
                ('senha', models.CharField(blank=True, max_length=6, null=True)),
                ('exame', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='exames.tiposexames')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PedidosExames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agendado', models.BooleanField(default=True)),
                ('data', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
                ('exames', models.ManyToManyField(to='exames.solicitacaoexame')),
            ],
        ),
    ]
