from django.db import models

# Create your models here.

class FarmAnimal(models.Model):
	animal_name = models.CharField(max_length = 15)
	nbr_legs = models.IntegerField(default=4)

	def __str__(self):
		return self.animal_name
