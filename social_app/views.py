from django.shortcuts import render,redirect,get_object_or_404
# from rest_framework import viewsets,filters
# from rest_framework.response import Response
# from rest_framework import status,exceptions
# from django.db import IntegrityError
from . models import Tags, Posts, CustomUser,Comments,Likes,Followers
# from . serializers import TagSerializer,PostSerializer,UserSeriaLizer,CommentSeriaLizer,LikeSeriaLizer,FollowSeriaLizer
# from rest_framework.decorators import api_view
from . forms import UserForm,TagForm, PostForm, UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])
            user.save()
            login(request,user)
            return redirect('view-posts')
    else:
        form=UserForm()
    return render(request, "users/create_user.html",{"form":form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("view-posts")
    else:
        form = AuthenticationForm
    return render(request,"users/login.html",{"form":form})


def logout_user(request):
    logout(request)
    return redirect("login-user")


def settings(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect("settings")
    else:
        form = UserUpdateForm(instance=user)
    return render(request,"users/settings.html",{"form":form})


def my_posts(request):
    user = request.user
    print("user is",user)
    
    posts = Posts.objects.filter(user=user)
    print(posts.count())
    return render(request, "posts/my_posts.html",{
        "posts":posts
    })

def edit_post(request,pk):
    posts = get_object_or_404(Posts,pk = pk,user = request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            form.save()
            return redirect("my-posts")
    else:
        form = PostForm(instance=posts)

    return render(request,"posts/edit_post.html",{"form":form})


def delete_post(request,pk):
    post = get_object_or_404(Posts, pk = pk, user = request.user)
    if request.method == "POST":
        post.delete()
        return redirect("my-posts")
    return render(request,"posts/delete_post.html",{"post":post})



# def profile(request,username):
#     user = get_object_or_404(CustomUser,username=username)
#     context = {
#         "profile_user":user,
#         "posts":user.posts_set.all().order_by("-created_at")
#     }
#     return render(request,"my_posts.html",context)

def followers(request):
    pass

def following(request):
    pass


def create_tag(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view-posts")
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
    return render(request, "posts/all_posts.html",{"posts":all_posts})

def like_post(request,post_id):
    post = get_object_or_404(Posts,id=post_id)
    
    like,created = Likes.objects.get_or_create(
        user = request.user,
        post = post
    )
    if not created:
        like.delete()
    return redirect("view-posts")

def comment_post(request,comment_id):
    post = get_object_or_404(Posts,id=comment_id)
    if request.method == "POST":
        comment = request.POST.get("content")
        if comment:
            Comments.objects.create(
                user = request.user,
                post = post,
                comment = comment
            )
            return redirect("view-posts")
    return render(request,"posts/comment_post.html",{"post":post})

def post_detail(request,post_id):
    post = Posts.objects.get(id = post_id)
    comments = Comments.objects.filter(post = post).order_by("created_at")
    return render(request, "posts/post_detail.html",{
        "post":post,
        "comments":comments
    })



    
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

