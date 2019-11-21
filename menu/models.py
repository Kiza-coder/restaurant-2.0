from django.db import models

# Create your models here.

class Burger(models.Model):
	name = models.CharField(max_length=100)
	composition = models.TextField(null=False)
	price = models.DecimalField(max_digits=5,decimal_places=2)

	class Meta:
		verbose_name="burger"
		ordering=['price']

	def __str__(self):
		return self.name
