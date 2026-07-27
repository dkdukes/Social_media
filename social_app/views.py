from django.shortcuts import render,redirect
# from rest_framework import viewsets,filters
# from rest_framework.response import Response
# from rest_framework import status,exceptions
# from django.db import IntegrityError
from . models import Tags, Posts, CustomUser,Comments,Likes,Followers
# from . serializers import TagSerializer,PostSerializer,UserSeriaLizer,CommentSeriaLizer,LikeSeriaLizer,FollowSeriaLizer
# from rest_framework.decorators import api_view
from . forms import UserForm,TagForm, PostForm

# Create your views here.

def view_users(request):
    all_users =CustomUser.objects.all()
    return render(request,"all_users.html",{"users":all_users})

def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all-users')
    else:
        form=UserForm()
    return render(request, "create_user.html",{"form":form})

def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("all-users")
    else:
        form=TagForm()
    return render(request,"create_tag.html",{"form":form})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            return redirect("view-posts")

    else:
        form = PostForm()

    return render(request,"create_post.html",{"form":form})

def view_posts(request):
    all_posts =Posts.objects.all()
    return render(request, "all_posts.html",{"posts":all_posts})


    
# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tags.objects.all()
#     serializer_class = TagSerializer


# class PostViewSet(viewsets.ModelViewSet):
#     queryset = Posts.objects.all()
#     serializer_class = PostSerializer


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = UserSeriaLizer

#     filter_backends = [filters.SearchFilter]
#     search_fields = ['username','user_first_name','user_last_name']

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comments.objects.all()
#     serializer_class = CommentSeriaLizer

# class LikeViewSet(viewsets.ModelViewSet):
#     queryset = Likes.objects.all()
#     serializer_class = LikeSeriaLizer

# class FollowerViewSet(viewsets.ModelViewSet):
#     queryset = Followers.objects.all()
#     serializer_class = FollowSeriaLizer

    
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

