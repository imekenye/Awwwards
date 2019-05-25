from rest_framework import serializers
from .models import Post
from accounts.models import Profile
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('post_image', 'title', 'content', 'url', 'date_posted', 'author')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'image',)
