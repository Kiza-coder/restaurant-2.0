from django.db import models
#Enum Choice type

choice_type = ('beef','chicken','fish')
# Create your models here.

class Burger(models.Model):
	name = models.CharField(max_length=100)
	type_burger = models.CharField(max_length=10,null=False,default=None,choices=choice_type)
	composition = models.TextField(null=False)
	price = models.DecimalField(max_digits=5,decimal_places=2)

	class Meta:
		verbose_name="burger"
		ordering=['price']

	def __str__(self):
		return self.name
