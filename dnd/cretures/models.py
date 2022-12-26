from django.db import models

# Create your models here.

class Cretures(models.Model):
	name = models.CharField(max_length=45)
	#attributes
	Strength = models.IntegerField()
	Constitution = models.IntegerField()
	Dexterity = models.IntegerField()
	Intelligence = models.IntegerField()
	Wisdom = models.IntegerField()
	Charisma = models.IntegerField()
	Charisma = models.IntegerField()
	proficiency =  models.IntegerField()
	


	def __str__(self):
		return f'{self.name}'