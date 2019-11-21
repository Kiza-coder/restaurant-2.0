from django.db import models

# Create your models here.

class ImageUrl(models.Model):
	url = models.CharField(max_length=100)
	order = models.PositiveIntegerField(unique=True)

	class Meta:
		verbose_name="url_image"
		ordering=['order']

	def __str__(self):
		return self.url
