from rest_framework import serializers

from .models import Post#import post models
#there are different kind of serializer
#ModelSerializer convert model into json
class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model=Post
		fields=['id','title','url','poster','created']
		#id is explicitly listed as field but it is included with eveny django model
		#this is saying if someone want to get post from database it can come out as model 
		#go through serializer  and eventually convert into json

	#tell what field from model we want to associate with api

