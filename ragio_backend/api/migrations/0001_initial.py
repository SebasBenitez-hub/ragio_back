# Generated by Django 3.0.3 on 2020-03-03 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreActividad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreFiscal', models.CharField(max_length=100)),
                ('nombreComercial', models.CharField(max_length=100)),
                ('poblacion', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('rfc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreServicio', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=50)),
                ('user_type', models.CharField(choices=[('A', 'Admin'), ('C', 'Colab')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Colab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreColab', models.CharField(max_length=100)),
                ('tituloProf', models.CharField(max_length=100)),
                ('correoColab', models.CharField(max_length=100)),
                ('telefonoColab', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='ActDiarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('desdeHora', models.TimeField()),
                ('hastaHora', models.TimeField()),
                ('observacionAdicional', models.CharField(default='', max_length=300)),
                ('porcentajeAvance', models.FloatField()),
                ('actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Act')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Cliente')),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Colab')),
                ('servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Servicio')),
            ],
        ),
        migrations.AddField(
            model_name='act',
            name='servicio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Servicio'),
        ),
    ]
