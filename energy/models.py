from django.db import models


class Drink(models.Model):
	brand = models.CharField(max_length= 250)
	name = models.CharField(max_length= 250)
	photo = models.CharField(max_length= 1000)
	brand_photo = models.CharField(max_length= 1000)


	def __str__(self):
		return self.brand + ' - ' + self.name

