# Generated by Django 5.0.6 on 2024-05-17 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ferremax_APP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoriaproducto',
            old_name='nombre_categoria',
            new_name='nombre',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='nombre_producto',
            new_name='nombre',
        ),
        migrations.AlterUniqueTogether(
            name='detallepedido',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='inventario',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='promocion',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='categoriaproducto',
            name='id_categoria',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='id_cliente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='especialidad',
            name='id_especialidad',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='estadopedido',
            name='id_estado_pedido',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='id_mensaje',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id_pedido',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='codigo_upc',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id_producto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sucursal',
            name='id_sucursal',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipopromocion',
            name='id_tipo_promocion',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='vendedor',
            name='id_vendedor',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
