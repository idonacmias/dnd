from django.db import models

# Create your models here.

class Player(models.Model):
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	
	adventurer = models.ForeignKey("Adventurer", on_delete=models.CASCADE)

	class Meta:
		unique_together = [['first_name', 'last_name']]

	def __str__(self):
		return f'{self.first_name} {self.last_name}'

class Creture(models.Model):
	name = models.CharField(max_length=45)
	#attributes
	Strength = models.IntegerField()
	Dexterity = models.IntegerField()
	Constitution = models.IntegerField()
	Intelligence = models.IntegerField()
	Wisdom = models.IntegerField()
	Charisma = models.IntegerField()
	
	hp = models.IntegerField()

	def __str__(self):
		return f'{self.name}'


class Adventurer(models.Model):

	creture = models.OneToOneField(Creture, on_delete=models.CASCADE)

	level = models.IntegerField()
	profession = models.CharField(max_length=25)
	races = models.CharField(max_length=25)
	skills_proficiency = models.ForeignKey("Skills_proficiency", on_delete=models.CASCADE)



	def __str__(self):
		return f'{self.creture.name}'


class Skills_proficiency(models.Model):
	NAME = [('one'), ('two')]
	name = models.CharField(max_length=25)
	value = models.IntegerField()

	def __str__(self):
		return f'{self.name}: {self.value}'




