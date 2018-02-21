from django.db import models

# Create your models here.
class Game(models.Model):
	name = models.CharField(max_length = 100)
	release_date = models.DateField()
	plateforms= models.CharField(max_length= 100)
	image = models.ImageField()

	def __str__(self):
		return self.name

 
		