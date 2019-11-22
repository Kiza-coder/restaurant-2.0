from django.db import models

# Create your models here.

choice_gender = (
	('1','Male'),('2','Female')
	)


class Contact(models.Model):
	name = models.CharField(max_length=100)
	firstname = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	gender = models.CharField(null=True,max_length=1,default=None,choices=choice_gender)
	message = models.TextField(null=False)


	def __str__(self):
		return self.name

