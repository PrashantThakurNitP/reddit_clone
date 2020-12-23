from django.shortcuts import render

# Create your views here.
#ability to list out all different post that are saved inside database
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
class PostList(generics.ListAPIView):#class based view that list out all informations
	queryset=Post.objects.all()
	#now specify what serilizer to be used for this view
	serializer_class=PostSerializer
