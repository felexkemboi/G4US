from django.db import models
from django.utils import timezone
from django.conf import settings
from django.urls import reverse

# Create your models here.

class Post(models.Model):
	subject =      models.CharField(max_length=50)
	message =      models.CharField(max_length=280)
	created_date = models.DateTimeField(default=timezone.now)


	"""def publish(self):
		self.published_date = timezone.now()
		self.save()"""

	def get_absolute_url(self):
		return reverse('detail', args = [str(self.id)])

	def __str__(self):
		return self.subject

class Comment(models.Model):
    post = models.ForeignKey('Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    """def approve(self):
        self.approved_comment = True
        self.save()"""

    def __str__(self):
        return self.text

