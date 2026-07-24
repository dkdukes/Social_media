from rest_framework import serializers
from .models import Posts,Tags, CustomUser,Comments,Likes,Followers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class UserSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

class CommentSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

class LikeSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

class FollowSeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Followers
        fields = '__all__'