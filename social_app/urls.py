from django.urls import path,include
# from rest_framework.routers import DefaultRouter
# from . import views
# from .views import TagViewSet,PostViewSet,UserViewSet,CommentViewSet,LikeViewSet,FollowerViewSet
from . import views
from django.contrib.auth import views as auth_views



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
    path("create-user/",views.create_user,name="create-user"),
    path("",views.login_user,name="login-user"),
    path("logout/",views.logout_user,name="logout-user"),
    path("tags/",views.create_tag,name="create-tag"),
    path("create-post/",views.create_post,name="create-post"),
    path("view-posts/",views.view_posts,name="view-posts"),
    path("post/<int:post_id>/like/",views.like_post,name="like-post"),
    path("post/<int:comment_id>/comment",views.comment_post,name="comment-post"),
    path("post/<int:post_id>/details",views.post_detail,name="post-detail"),
    path("settings/",views.settings,name="settings"),
    path("my_posts/",views.my_posts,name="my-posts"),
    path("followers/",views.followers,name="followers"),
    path("following/",views.following,name="following"),
    path("settings/password/",auth_views.PasswordChangeView.as_view(template_name="users/password_change.html",success_url="/settings/password/done/"),name="password-change"),
    path("settings/password/done/",auth_views.PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),name="password-change-done"),
    path("post/<int:pk>/edit/",views.edit_post,name="edit-post"),
    path("posts/<int:pk>/delete/",views.delete_post,name="delete-post")

]
