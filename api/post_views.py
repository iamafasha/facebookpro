from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from post.models import Post , Comment ,PostImage, PostLike
from.post_serializers import PostSerializers
from rest_framework import permissions

class PostListView(ListCreateAPIView):
    serializer_class = PostSerializers

    def perform_create(self, serializer):
        serializer.save()
    def get_queryset(self):
        return Post.objects.all()

class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class = PostSerializers
    lookup_field = "id"

    def get_queryset(self):
        return Post.objects.all()