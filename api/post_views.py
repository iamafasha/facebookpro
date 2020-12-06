from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from post.models import Post , Comment ,PostMedia, PostLike
from.post_serializers import PostSerializers ,CommentSerializers
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class PostListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = PostSerializers

    def perform_create(self, serializer):
        print(serializer)
        serializer.save()
    def get_queryset(self):
        return Post.objects.filter(approved=True ).order_by('-published_date')

class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    
    serializer_class = PostSerializers
    lookup_field = "id"

    def get_queryset(self):
        return Post.objects.filter(approved=True)


class CommentListView(ListCreateAPIView):
    serializer_class = CommentSerializers
    permission_classes = [IsAuthenticated|ReadOnly]
    
    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post=Post.objects.get(id = post_id)
        user =  self.request.user
        serializer.save(reply_to = post, author=user )

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        if self.request.user.is_authenticated:
            if self.request.user.is_staff or self.request.user.id == Post.objects.get(id=post_id).author.id:
                return Comment.objects.filter(reply_to=post_id)
            return Comment.objects.filter(reply_to=post_id ,approved=True) | Comment.objects.filter(reply_to=post_id ,author = self.request.user)
        return Comment.objects.filter(reply_to=post_id ,approved=True)
        
    def get_serializer_class(self):
        post_id = self.kwargs['post_id']
        # Check if owner of post 
        if self.request.user.is_staff or self.request.user.id == Post.objects.get(id=post_id).author.id:
            return PostOwnerComentSerializers
        return CommentSerializers

class CommentDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    serializer_class = CommentSerializers
    lookup_field = "id"
    def get_queryset(self):
        return Comment.objects.filter(approved=True)