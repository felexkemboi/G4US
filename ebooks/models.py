from django.db import models
from django.utils import timezone


class Document(models.Model):
	description  = models.CharField(max_length=255,blank=True)
	file         = models.FileField(upload_to='media/')
	name         = models.CharField(max_length = 200)
	created_at   = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.name