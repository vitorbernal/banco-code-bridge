# Generated by Django 4.2.2 on 2023-06-10 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0003_alter_clientes_endereco_alter_clientes_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldo', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='saldo do cliente')),
                ('data_abertura', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='clientes.clientes')),
            ],
        ),
    ]
