from django.contrib import admin
from .models import TipoPromocion, Especialidad, CategoriaProducto, Usuario, Cliente, Vendedor, \
                    Sucursal, Producto, Inventario, EstadoPedido, Pedido, DetallePedido, \
                    Promocion, Mensaje

@admin.register(TipoPromocion)
class TipoPromocionAdmin(admin.ModelAdmin):
    pass

@admin.register(Especialidad)
class EspecialidadAdmin(admin.ModelAdmin):
    pass

@admin.register(CategoriaProducto)
class CategoriaProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    pass

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    pass

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    pass

@admin.register(EstadoPedido)
class EstadoPedidoAdmin(admin.ModelAdmin):
    pass

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    pass

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    pass

@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    pass

@admin.register(Mensaje)
class MensajeAdmin(admin.ModelAdmin):
    pass
