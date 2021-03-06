from django.conf import settings
from django.contrib.gis.db import models
from django.urls import reverse

class Basin(models.Model):
	user					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	codigo 					= models.IntegerField(unique=False,null=True,blank=True)
	nombre 					= models.CharField(max_length = 120,null = True,blank=True)
	direccion				= models.CharField(max_length = 120,null = True,blank=True)
	tipo_sensor 			= models.IntegerField(null = True,blank=True,choices =((0,'Ultrasonido'),(1,'Radar')))#
	vel_sup 				= models.IntegerField(null=True,blank=True)
	area 					= models.FloatField(max_length = 120,null = True,blank=True)
	subcuenca 				= models.CharField(max_length = 120,null = True,blank=True)
	barrio 					= models.CharField(max_length = 120,null = True,blank=True)
	source 					= models.CharField(max_length = 120,null = True,blank=True)
	l_cuenca 				= models.FloatField(max_length = 120,null = True,blank=True)
	longitud_basin 			= models.FloatField(max_length = 120,null = True,blank=True)
	fecha_instalacion 		= models.DateField(null = True,blank=True)
	h_cauce_max 			= models.FloatField(max_length = 120,null = True,blank=True)
	pend_cuenca 			= models.FloatField(max_length = 120,null = True,blank=True)
	hmax 					= models.FloatField(max_length = 120,null = True,blank=True)
	kml_path 				= models.CharField(max_length = 120,null = True,blank=True)
	l_cauce 				= models.FloatField(max_length = 120,null = True,blank=True)
	perimetro 				= models.FloatField(max_length = 120,null = True,blank=True)
	municipio 				= models.CharField(max_length = 120,null = True,blank=True)
	hmean 					= models.CharField(max_length = 120,null = True,blank=True)
	flag_modelo_estadistico = models.IntegerField(null=True,blank=True,choices=((1,'si'),(0,'no')))#
	dpx 					= models.FloatField(max_length = 120,null = True,blank=True)
	camara_path 			= models.CharField(max_length = 120,null = True,blank=True)
	rain_path 				= models.CharField(max_length = 120,null = True,blank=True)
	pic_path 				= models.CharField(max_length = 120,null = True,blank=True)
	latitud 				= models.FloatField(max_length = 120,null = True,blank=True)
	polygon_path 			= models.CharField(max_length = 120,null = True,blank=True)
	centro_x 				= models.FloatField(max_length = 120,null = True,blank=True)
	centro_y 				= models.FloatField(max_length = 120,null = True,blank=True)
	pluvios 				= models.CharField(max_length = 120,null = True,blank=True)
	red 					= models.CharField(max_length = 120,null = True,blank=True)
	telefono_contacto 		= models.BigIntegerField(null = True,blank=True)
	offset_old 				= models.FloatField(max_length = 120,null = True,blank=True)
	offset 				= models.FloatField(max_length = 120,null = True,blank=True)
	flag_modelo_wmf 		= models.IntegerField(null = True,blank=True,choices=((1,'si'),(0,'no')))#
	net_path 				= models.CharField(max_length = 120,null = True,blank=True)
	x_sensor 				= models.FloatField(max_length = 120,null = True,blank=True)
	latitud_basin 			= models.FloatField(max_length = 120,null = True,blank=True)
	sirena 					= models.CharField(max_length = 120,null = True,blank=True,choices=((1,'si'),(0,'no')))#
	estado 					= models.CharField(max_length = 1,null = True,blank=True,choices=(('A','Activa'),('P','Pendiente'),('I','Inactiva')))
	clase 					= models.CharField(max_length = 120,null = True,blank=True)
	longitud 				= models.FloatField(max_length = 120,null = True,blank=True)
	slug 					= models.CharField(max_length = 120,null = True,blank=True,unique=True)# for unique
	nombre_contacto 		= models.CharField(max_length = 120,null = True,blank=True)
	hmin 					= models.FloatField(max_length = 120,null = True,blank=True)
	pend_cauce 				= models.FloatField(max_length = 120,null = True,blank=True)
	nc_path 				= models.CharField(max_length = 120,null = True,blank=True)
	stream_path 			= models.CharField(max_length = 120,null = True,blank=True)
	n1 						= models.FloatField(max_length = 120,null = True,blank=True)
	n2 						= models.FloatField(max_length = 120,null = True,blank=True)
	n3 						= models.FloatField(max_length = 120,null = True,blank=True)
	n4 						= models.FloatField(max_length = 120,null = True,blank=True)
	l_tot_cauces 			= models.FloatField(max_length = 120,null = True,blank=True)
	timestamp				= models.DateTimeField(auto_now_add=True)
	updated					= models.DateTimeField(auto_now=True)
	water_level_history_path = models.CharField(max_length = 120,null = True,blank=True)
	radar_rain_history_path = models.CharField(max_length = 120,null = True,blank=True)
	statistical_model_path  = models.CharField(max_length = 120,null = True,blank=True)
	picture_path            = models.CharField(max_length = 120,null = True,blank=True)
	camera_path             = models.CharField(max_length = 120,null = True,blank=True)
	three_hours_image_path  = models.CharField(max_length = 120,null = True,blank=True)
	one_day_image_path      = models.CharField(max_length = 120,null = True,blank=True)
	three_days_image_path   = models.CharField(max_length = 120,null = True,blank=True)
	monthly_image_path      = models.CharField(max_length = 120,null = True,blank=True)
	wmf_image_path          = models.CharField(max_length = 120,null = True,blank=True)
	basin_mask_path         = models.CharField(max_length = 120,null = True,blank=True)
	basin_polygon           = models.PolygonField(null=True,blank=True)
	def __str__(self):
		return self.slug

	@property
	def title(self):
		return self.nombre



class Stations(models.Model):
	user					= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	codigo 					= models.IntegerField(unique=False,null=True,blank=True)
	nombre 					= models.CharField(max_length = 120,null = True,blank=True)
	direccion				= models.CharField(max_length = 120,null = True,blank=True)
	tipo_sensor 			= models.IntegerField(null = True,blank=True,choices =((0,'Ultrasonido'),(1,'Radar')))#
	vel_sup 				= models.IntegerField(null=True,blank=True)
	area 					= models.FloatField(max_length = 120,null = True,blank=True)
	subcuenca 				= models.CharField(max_length = 120,null = True,blank=True)
	barrio 					= models.CharField(max_length = 120,null = True,blank=True)
	source 					= models.CharField(max_length = 120,null = True,blank=True)
	l_cuenca 				= models.FloatField(max_length = 120,null = True,blank=True)
	longitud_basin 			= models.FloatField(max_length = 120,null = True,blank=True)
	fecha_instalacion 		= models.DateField(null = True,blank=True)
	h_cauce_max 			= models.FloatField(max_length = 120,null = True,blank=True)
	pend_cuenca 			= models.FloatField(max_length = 120,null = True,blank=True)
	hmax 					= models.FloatField(max_length = 120,null = True,blank=True)
	kml_path 				= models.CharField(max_length = 120,null = True,blank=True)
	l_cauce 				= models.FloatField(max_length = 120,null = True,blank=True)
	perimetro 				= models.FloatField(max_length = 120,null = True,blank=True)
	municipio 				= models.CharField(max_length = 120,null = True,blank=True)
	hmean 					= models.CharField(max_length = 120,null = True,blank=True)
	flag_modelo_estadistico = models.IntegerField(null=True,blank=True,choices=((1,'si'),(0,'no')))#
	dpx 					= models.FloatField(max_length = 120,null = True,blank=True)
	camara_path 			= models.CharField(max_length = 120,null = True,blank=True)
	rain_path 				= models.CharField(max_length = 120,null = True,blank=True)
	pic_path 				= models.CharField(max_length = 120,null = True,blank=True)
	latitud 				= models.FloatField(max_length = 120,null = True,blank=True)
	polygon_path 			= models.CharField(max_length = 120,null = True,blank=True)
	centro_x 				= models.FloatField(max_length = 120,null = True,blank=True)
	centro_y 				= models.FloatField(max_length = 120,null = True,blank=True)
	pluvios 				= models.CharField(max_length = 120,null = True,blank=True)
	red 					= models.CharField(max_length = 120,null = True,blank=True)
	telefono_contacto 		= models.BigIntegerField(null = True,blank=True)
	offset_old 				= models.FloatField(max_length = 120,null = True,blank=True)
	offset 				= models.FloatField(max_length = 120,null = True,blank=True)
	flag_modelo_wmf 		= models.IntegerField(null = True,blank=True,choices=((1,'si'),(0,'no')))#
	net_path 				= models.CharField(max_length = 120,null = True,blank=True)
	x_sensor 				= models.FloatField(max_length = 120,null = True,blank=True)
	latitud_basin 			= models.FloatField(max_length = 120,null = True,blank=True)
	sirena 					= models.CharField(max_length = 120,null = True,blank=True,choices=((1,'si'),(0,'no')))#
	estado 					= models.CharField(max_length = 1,null = True,blank=True,choices=(('A','Activa'),('P','Pendiente'),('I','Inactiva')))
	clase 					= models.CharField(max_length = 120,null = True,blank=True)
	longitud 				= models.FloatField(max_length = 120,null = True,blank=True)
	slug 					= models.CharField(max_length = 120,null = True,blank=True,unique=True)# for unique
	nombre_contacto 		= models.CharField(max_length = 120,null = True,blank=True)
	hmin 					= models.FloatField(max_length = 120,null = True,blank=True)
	pend_cauce 				= models.FloatField(max_length = 120,null = True,blank=True)
	nc_path 				= models.CharField(max_length = 120,null = True,blank=True)
	stream_path 			= models.CharField(max_length = 120,null = True,blank=True)
	n1 						= models.FloatField(max_length = 120,null = True,blank=True)
	n2 						= models.FloatField(max_length = 120,null = True,blank=True)
	n3 						= models.FloatField(max_length = 120,null = True,blank=True)
	n4 						= models.FloatField(max_length = 120,null = True,blank=True)
	l_tot_cauces 			= models.FloatField(max_length = 120,null = True,blank=True)
	timestamp				= models.DateTimeField(auto_now_add=True)
	updated					= models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.slug

	@property
	def title(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse("meta:detalle",kwargs = {'slug':self.slug})
