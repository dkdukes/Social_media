from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status,exceptions
from django.db import IntegrityError
from . models import Tags, Posts, CustomUser,Comments,Likes,Followers
from . serializers import TagSerializer,PostSerializer,UserSeriaLizer,CommentSeriaLizer,LikeSeriaLizer,FollowSeriaLizer
from rest_framework.decorators import api_view

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all()
    serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSeriaLizer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSeriaLizer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Likes.objects.all()
    serializer_class = LikeSeriaLizer

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Followers.objects.all()
    serializer_class = FollowSeriaLizer

    
# @api_view(["GET","POST"])
# def tag_create_list(request):
#     if request.method == "GET":
#         tags = Tags.objects.all()
#         serializer = TagSerializer(tags, many = True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TagSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
# @api_view(["GET","POST"])
# def post_create_list(request):
#     if request.method == "GET":
#         posts = Posts.objects.all()
#         serializer = PostSerializer(posts, many = True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = PostSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

