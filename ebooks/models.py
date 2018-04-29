from django.db import models
from django.utils import timezone


class Document(models.Model):
	name         = models.CharField(max_length = 200)
	description  = models.CharField(max_length=255,blank=True)
	file         = models.FileField(upload_to='')
	created_at   = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return str(self.description)
		