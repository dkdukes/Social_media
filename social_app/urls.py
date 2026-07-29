from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from . import views
# from .views import TagViewSet,PostViewSet,UserViewSet,CommentViewSet,LikeViewSet,FollowerViewSet
from . import views



# urlpatterns = [
#     path('tags/', views.tag_create_list,name="create-tag"),
#     path('posts/',views.post_create_list,name="create-post"),
#     path('posts/int<pk>,')
# ]

# router = DefaultRouter()
# router.register(r'tags',TagViewSet,basename="tags")
# router.register(r'posts',PostViewSet,basename="posts")
# router.register(r'users',UserViewSet,basename="users")
# router.register(r'comments',CommentViewSet,basename="comments")
# router.register(r'likes',LikeViewSet,basename="likes")
# router.register(r'followers',FollowerViewSet,basename="followers")

urlpatterns = [
    # path("v1/",include(router.urls)),
    path("create/",views.create_user,name="create-user"),
    path("users/",views.view_users,name="all-users"),
    path("tags/",views.create_tag,name="create-tag"),
    path("posts/create-post/",views.create_post,name="create-post"),
    path("posts/view-posts/",views.view_posts,name="view-posts"),
    path("post/<int:post_id>/like/",views.like_post,name="like-post"),
    path("post/<int:comment_id>/comment",views.comment_post,name="comment-post"),
    path("post/<int:post_id>/details",views.post_detail,name="post-detail")

]
