from rest_framework import serializers

from .models import Post,Vote#import post and vote models
#there are different kind of serializer
#ModelSerializer convert model into json
class PostSerializer(serializers.ModelSerializer):
	poster=serializers.ReadOnlyField(source='poster.username')
	poster_id=serializers.ReadOnlyField(source='poster.id')
	#we make the field read only field and we have specified source from where data will come
	class Meta:
		model=Post
		fields=['id','title','url','poster','poster_id','created']
		#id is explicitly listed as field but it is included with eveny django model
		#this is saying if someone want to get post from database it can come out as model 
		#go through serializer  and eventually convert into json

	#tell what field from model we want to associate with api

class VoteSerializer(serializers.ModelSerializer):
	
	class Meta:
		model=Vote
		fields=['id']
		#we don't decide username when we vote , it will be contained in url