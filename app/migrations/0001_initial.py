# Generated by Django 3.2.8 on 2022-10-12 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Huespedes',
            fields=[
                ('rut', models.CharField(max_length=13, primary_key=True, serialize=False, verbose_name='Rut Huesped')),
                ('nombre_completo', models.CharField(max_length=50, null=True, verbose_name='Nombre Completo')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], default='', max_length=1, null=True, verbose_name='Sexo')),
                ('fecha_nacimiento', models.DateField(null=True, verbose_name='Fecha de nacimiento (dd/mm/yyyy)')),
                ('telefono_contacto', models.CharField(max_length=15, null=True, verbose_name='Teléfono')),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('nombre_usuario', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Nombre Usuario')),
                ('contrasenna', models.CharField(max_length=20, verbose_name='Contraseña')),
                ('correo_electronico', models.CharField(max_length=20, verbose_name='Correo Electrónico')),
            ],
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='ID de Reserva')),
                ('fecha_reserva', models.DateField(null=True, verbose_name='Fecha de reserva (dd/mm/yyyy)')),
                ('nro_habitacion', models.IntegerField(default=0, verbose_name='Número de habitación')),
                ('timestamp', models.DateField(auto_now_add=True, null=True, verbose_name='')),
                ('rut_huesped', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.huespedes')),
            ],
        ),
    ]