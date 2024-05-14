from django.db import models

class TipoPromocion(models.Model):
    id_tipo_promocion = models.IntegerField(primary_key=True)
    tipo_promocion = models.CharField(max_length=255)

class Especialidad(models.Model):
    id_especialidad = models.IntegerField(primary_key=True)
    nombre_especialidad = models.CharField(max_length=255)

class CategoriaProducto(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    nombre_categoria = models.CharField(max_length=255)

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    contrasenia = models.CharField(max_length=255)
    rol = models.CharField(max_length=255)

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Vendedor(models.Model):
    id_vendedor = models.IntegerField(primary_key=True)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_vendedor = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class Sucursal(models.Model):
    id_sucursal = models.IntegerField(primary_key=True)
    direccion = models.CharField(max_length=255)
    telefono = models.IntegerField()

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    id_especialidad = models.ForeignKey(Especialidad, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(CategoriaProducto, on_delete=models.CASCADE)
    codigo_upc = models.IntegerField()
    nombre_producto = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)

class Inventario(models.Model):
    id_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    class Meta:
        unique_together = ('id_sucursal', 'id_producto')

class EstadoPedido(models.Model):
    id_estado_pedido = models.IntegerField(primary_key=True)
    estado_pedido = models.CharField(max_length=255)

class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_estado_pedido = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE)
    fecha_pedido = models.DateField()
    moneda = models.FloatField()
    conversion = models.FloatField()

class DetallePedido(models.Model):
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    precio_unitario = models.FloatField()
    cantidad = models.IntegerField()
    class Meta:
        unique_together = ('id_pedido', 'id_producto')

class Promocion(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_tipo_promocion = models.ForeignKey(TipoPromocion, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    class Meta:
        unique_together = ('id_producto', 'id_tipo_promocion')

class Mensaje(models.Model):
    id_mensaje = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    mensaje = models.CharField(max_length=255)
    fecha_hora_envio = models.DateField()