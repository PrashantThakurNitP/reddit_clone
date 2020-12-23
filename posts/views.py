from django.shortcuts import render

# Create your views here.
#ability to list out all different post that are saved inside database
from rest_framework import generics,permissions
from .models import Post
from .serializers import PostSerializer
class PostList(generics.ListCreateAPIView):#class based view that list out all informations
	queryset=Post.objects.all()
	#now specify what serilizer to be used for this view
	serializer_class=PostSerializer
	# make sure that only logged in user can make call to api
	#permission_classes=[permissions.IsAuthenticated] # this tell Authentication credentials were not provided
		
	
	permission_classes=[permissions.IsAuthenticatedOrReadOnly]# it allow to read but not write if not authenticated
	def perform_create(self,serializer):#name of this function must be same
		serializer.save(poster=self.request.user)
