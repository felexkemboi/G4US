from django.contrib import admin
from .models import Post
from .models import Comment
# Register your models here.
#admin.site.register(Post)

#from django.contrib import admin
from . import models
class CommentInline(admin.StackedInline):
	model = models.Comment

class PostAdmin(admin.ModelAdmin):
	inlines = [
	CommentInline,
	]
	
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment)
