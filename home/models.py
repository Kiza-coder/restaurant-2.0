from django.db import models

# Create your models here.

class Event(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(null=True)
	date = models.DateTimeField(verbose_name='Date dexpiration')

	class Meta:
		verbose_name="event"
		ordering=['date']

	def __str__(self):
		return self.title


class Promotion(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(null=True)
	date = models.DateTimeField(verbose_name='Date dexpiration')


	class Meta:
		verbose_name="promo"
		ordering=['date']

	def __str__(self):
		return self.title
