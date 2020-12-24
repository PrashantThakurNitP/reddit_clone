from django.shortcuts import render

# Create your views here.
#ability to list out all different post that are saved inside database
from rest_framework import generics,permissions,mixins,status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Post,Vote #import vote and post object
from .serializers import PostSerializer,VoteSerializer
class PostList(generics.ListCreateAPIView):#class based view that list out all informations
	queryset=Post.objects.all()
	#now specify what serilizer to be used for this view
	serializer_class=PostSerializer
	# make sure that only logged in user can make call to api
	#permission_classes=[permissions.IsAuthenticated] # this tell Authentication credentials were not provided
		
	
	permission_classes=[permissions.IsAuthenticatedOrReadOnly]# it allow to read but not write if not authenticated
	def perform_create(self,serializer):#name of this function must be same
		serializer.save(poster=self.request.user)
class PostRetrieveDestroy(generics.RetrieveDestroyAPIView):
	queryset=Post.objects.all()
	serializer_class=PostSerializer
	permission_classes=[permissions.IsAuthenticatedOrReadOnly]# it allow to read but not write if not authenticated
	def delete(self,request,*args,**kwargs):
		post=Post.objects.filter(pk=self.kwargs['pk'],poster=self.request.user)
		if post.exists():
			return self.destroy(request,*args,**kwargs)
		else:
			raise ValidationError("this isn't your post to delete, BRUH!:)")


	

class VoteCreate(generics.CreateAPIView,mixins.DestroyModelMixin):# list is not taken as no one want to see individual vote  
	#this will make new vote object
	
	serializer_class=VoteSerializer	
	permission_classes=[permissions.IsAuthenticated]# someone must be authenticated to use this
	#we are looking or particular object and particular vote
	def get_queryset(self):
		user=self.request.user
		post=Post.objects.get(pk=self.kwargs['pk'])#self.kwargs['pk'] is make of getting pk ie primary key of post 
		#that was passed through url 
		return Vote.objects.filter(voter=user,post=post)
	def perform_create(self,serializer):#name of this function must be same
		if self.get_queryset().exists():
			raise ValidationError("You have already voted for this post:)")
		serializer.save(voter=self.request.user,post=Post.objects.get(pk=self.kwargs['pk']))
	def delete(self,request,*args,**kwargs):#this f will add delete buttom to ddelete vote  in api/posts/vote_id/vote
		if self.get_queryset().exists():
			self.get_queryset().delete()
			return Response(status=status.HTTP_204_NO_CONTENT)
		else:
			raise ValidationError("You never voted for this post:)")

