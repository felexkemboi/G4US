from django.contrib import admin

from .models import Document
# Register your models here.
#admin.site.register(Post)

#from django.contrib import admin
"""class CommentInline(admin.StackedInline):
	model = models.Comment"""

#class PostAdmin(admin.ModelAdmin):
		
#admin.site.register(models.Post, PostAdmin)
admin.site.register(Document)
