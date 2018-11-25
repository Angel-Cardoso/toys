from django.db import models
from django.conf import settings

# Create your models here.
class Areas(models.Model):
	nombre_area = models.CharField(max_length = 40)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_area)

class Lineas(models.Model):
	area = models.ForeignKey(Areas, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.id)

class Piezas_gral(models.Model):
	nombre_pieza = models.CharField(max_length = 40)
	proveedor = models.CharField(max_length = 40)
	precio = models.FloatField()
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_pieza)

class Piezas_indiv(models.Model):
	nombre_pieza = models.ForeignKey(Piezas_gral, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_pieza)

class Productos_gral(models.Model):
	nombre_producto = models.CharField(max_length = 40)
	precio = models.FloatField()
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_producto)

class Productos_indiv(models.Model):

	# Este valor nos permite hacer una seleccion entre una serie
	# de opciones
	RADIO_CHOICES = (
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5),
		)
	FABRICA_CHOICES = (
		('TIJ', 'Tijuana'),
		('ROS', 'Rosarito'),
		('TEC', 'Tecate'),
		)

	# Campos chidos
	nombre_producto = models.ForeignKey(Productos_gral, on_delete=models.CASCADE)
	linea = models.ForeignKey(Lineas, on_delete=models.CASCADE, default = 1)
	
	# Campos de evaluación
	resistencia = models.IntegerField(choices = RADIO_CHOICES, default = 1)
	presentacion = models.IntegerField(choices = RADIO_CHOICES, default = 1)
	tamaño = models.IntegerField(choices = RADIO_CHOICES, default = 1)
	movilidad = models.IntegerField(choices = RADIO_CHOICES, default = 1)
	empaque = models.IntegerField(choices = RADIO_CHOICES, default = 1)
	fabrica = models.CharField(max_length = 40, choices = FABRICA_CHOICES, default = 'TIJ')
	# Función que calcula su calidad
	def _get_calificacion(self):
		return self.resistencia+self.presentacion+self.tamaño+self.movilidad+self.empaque
	# calificacion de calidad segun sus resultados
	calificacion = property(_get_calificacion)

	# Función que genera la etiqueta
	def _get_etiqueta(self):
		if self.calificacion <= 20:
			if self.id < 10:
				etiqueta = "TOYS" + "0" + str(self.id) + str(self.linea) + self.fabrica + "NOPE"
			else:
				etiqueta = "TOYS" + str(self.id) + str(self.linea) + self.fabrica + "NOPE"
		else:
			if self.id < 10:
				etiqueta = "TOYS" + "0" + str(self.id) + str(self.linea) + self.fabrica + "YEPA"
			else: 
				etiqueta = "TOYS" + str(self.id) + str(self.linea) + self.fabrica + "YEPA"
		return etiqueta
	# YEP para productos aprobados, NOPE para no aprobados
	etiqueta = property(_get_etiqueta)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_producto)

class Sexos(models.Model):
	sexo = models.CharField(max_length = 20)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.sexo)

class Estados(models.Model):
	estado = models.CharField(max_length = 20)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.estado)

# Probablemente este modelo quede inutil por un tiempo
class Cargos(models.Model):
	nombre_cargo = models. CharField(max_length = 20)
	descripcion = models.CharField(max_length = 100)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.nombre_cargo)

# El modelo Personal es remplazado por el modelo users que tiene django
# Cuando ampliemos el modelo users, probablemente nos sirva
# así que aquí lo dejo
# class Personal(models.Model):
# 	nombre_personal = models.CharField(max_length = 40)
# 	edad = models.IntegerField()
# 	sexo = models.ForeignKey(Sexos, on_delete=models.CASCADE)
# 	telefono = models.IntegerField()
# 	cargo = models.ForeignKey(Cargos, on_delete=models.CASCADE)
# 	fecha_registro = models.DateTimeField(auto_now_add = True)
# 	def __str__(self):
# 		return str(self.nombre_personal)

class Producto_pieza(models.Model):
	pieza = models.ForeignKey(Piezas_indiv, on_delete=models.CASCADE)
	producto = models.ForeignKey(Productos_indiv, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.id)

class Jefe_linea(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
	linea = models.ForeignKey(Lineas, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.personal)

class Jefe_area(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
	area = models.ForeignKey(Areas, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.personal)

class Orden_almacen(models.Model):
	# Este campo user se deberá poner autimaticamente, posteriormente
	# será por el usuario a quién se le entrega el material
	# y tendrá otro, de quien realiza la orden
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
	jefe_linea = models.ForeignKey(Jefe_linea, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	estado = models.ForeignKey(Estados, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.id)

class Pieza_orden(models.Model):
	pieza = models.ForeignKey(Piezas_indiv, on_delete=models.CASCADE)
	orden = models.ForeignKey(Orden_almacen, on_delete=models.CASCADE)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.id)

class Lotes(models.Model):
	FABRICA_CHOICES = (
		('TIJ', 'Tijuana'),
		('ROS', 'Rosarito'),
		('TEC', 'Tecate'),
		)
	linea = models.ForeignKey(Lineas, on_delete=models.CASCADE, default = 1)
	destino = models.CharField(max_length = 40, blank = True, default = 'sin destino')
	fabrica = models.CharField(max_length = 40, choices = FABRICA_CHOICES, default = 'TIJ')
	# Funcion que genera las etiquetas del lote
	def _get_etiqueta(self):
		if self.destino == "sin destino":
			if self.id < 10:
				etiqueta = "TOYS" + "0" + str(self.id) + str(self.linea) + self.fabrica + "-" +"NOP"
			else: 
				etiqueta = "TOYS" + str(self.id) + str(self.linea) + self.fabrica + "-" +"NOP"
		else:
			letras = self.destino[0:3]
			if self.id < 10:
				etiqueta = "TOYS" + "0" + str(self.id) + str(self.linea) + self.fabrica + "-" + letras.upper()			
			else:
				etiqueta = "TOYS" + str(self.id) + str(self.linea) + self.fabrica + "-" + letras.upper()
		return etiqueta
	# YEP para productos aprobados, NOPE para no aprobados
	etiqueta = property(_get_etiqueta)
	fecha_registro = models.DateTimeField(auto_now_add = True)
	def __str__(self):
		return str(self.id)