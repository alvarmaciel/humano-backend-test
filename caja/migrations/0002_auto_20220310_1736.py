# Generated by Django 3.2 on 2022-03-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venta',
            old_name='monto_pago',
            new_name='monto_total',
        ),
        migrations.RemoveField(
            model_name='itemventa',
            name='sub_total',
        ),
        migrations.AddField(
            model_name='itemventa',
            name='parcial',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='venta',
            name='recargo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True),
        ),
        migrations.AlterField(
            model_name='venta',
            name='bonificacion',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=9, null=True),
        ),
    ]
