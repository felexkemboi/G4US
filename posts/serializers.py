from rest_framework import serializers
from .models import Post

class PostSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = ( 'subject','message','created_date')


       