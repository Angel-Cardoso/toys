from django.contrib import admin
from .models import Piezas_gral
from .models import Piezas_indiv
from .models import Productos_gral
from .models import Productos_indiv
from .models import Sexos
from .models import Estados
# from .models import Personal # Este modelo está inutilizado de momento
# from .models import Producto_pieza
from .models import Areas
from .models import Lineas
from .models import Jefe_linea
from .models import Jefe_area
from .models import Orden_almacen
from .models import Lotes

# Register your models here.
admin.site.register(Piezas_gral)
admin.site.register(Piezas_indiv)
admin.site.register(Productos_gral)
admin.site.register(Productos_indiv)
admin.site.register(Sexos)
admin.site.register(Estados)
# admin.site.register(Personal) # Este modelo esta inutilizado de momento
# admin.site.register(Producto_pieza) # Este model ha sido reemplazado por un ManyToManyField
admin.site.register(Areas)
admin.site.register(Lineas)
admin.site.register(Jefe_linea)
admin.site.register(Jefe_area)
admin.site.register(Orden_almacen)
admin.site.register(Lotes)
# Modelos presentes:

# Piezas_gral
# Piezas_indiv
# Productos_gral
# Productos_indiv
# Sexos
# Estados
# Cargos
# Personal
# Producto_pieza
# Areas
# Lineas
# Jefe_linea
# Jefe_area
# Orden_almacen
# Pieza_orden  
