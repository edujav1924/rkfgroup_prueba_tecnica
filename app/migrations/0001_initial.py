# Generated by Django 4.2.7 on 2023-11-19 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=120)),
                ('nombrefactura', models.CharField(max_length=300)),
                ('nombrefantasia', models.CharField(max_length=300)),
                ('canalobj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.canal')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido_numero', models.BigIntegerField(unique=True)),
                ('doc_tipo', models.CharField(max_length=80)),
                ('doc_fecha', models.DateField()),
                ('doc_numero', models.BigIntegerField(default=0)),
                ('anulado_040', models.BooleanField(default=False)),
                ('anulado_040_fecha', models.DateTimeField(null=True)),
                ('anulado_040_por_gecos', models.CharField(max_length=120, null=True)),
                ('pdvobj', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('prod_marca', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Precios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField()),
                ('fecha_vigencia', models.DateField()),
                ('articuloobj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
                ('canalobj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.canal')),
            ],
        ),
        migrations.CreateModel(
            name='OrdersDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_original', models.IntegerField()),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.FloatField()),
                ('iva_10', models.FloatField()),
                ('gravada_10', models.FloatField()),
                ('iva_5', models.FloatField()),
                ('gravada_5', models.FloatField()),
                ('exenta', models.FloatField()),
                ('anulado_040', models.BooleanField(default=False)),
                ('anulado_040_fecha', models.DateTimeField(null=True)),
                ('anulado_040_por_gecos', models.CharField(max_length=120, null=True)),
                ('artobj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
                ('orderobj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.orders')),
            ],
        ),
    ]
