# Generated by Django 3.2 on 2022-02-20 19:00

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socies', '0001_initial'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, max_length=500, null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=9)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('cantidad_vendida', models.IntegerField(default=0, null=True)),
                ('socie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='socie', to='socies.socie')),
            ],
            options={
                'ordering': ('nombre',),
            },
        ),
        migrations.CreateModel(
            name='UnidadDeMedida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unidad', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos_tageados', to='producto.producto')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_tipodeproducto_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='producto',
            name='tipo',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', related_name='tipos', through='producto.TipoDeProducto', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='producto',
            name='unidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unidades', to='producto.unidaddemedida'),
        ),
    ]
