from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from post.models import Post , Comment ,PostMedia, PostLike
from .post_serializers import PostSerializers ,CommentSerializers , PostOwnerComentSerializers ,PostOwnerPostSerializers
from .permissions import IsAuthenticated, IsSuperUser, IsOwner, ReadOnly 


class PostListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated|ReadOnly]

    def perform_create(self, serializer):
        serializer.save()
    def get_queryset(self):
        # If staff get all the posts
        # else if user get all other people's approved posts and all(approved and unapproved) your posts
        # else if not authenticated return all approved posts.
        if self.request.user.is_staff:
            return Post.objects.all().order_by('-published_date')
        elif self.request.user.is_authenticated:
            posts= Post.objects.filter(approved=True) | Post.objects.filter(author=self.request.user)
            return posts.order_by('-published_date')
        else:
            return Post.objects.filter(approved=True ).order_by('-published_date')

    def get_serializer_class(self):
        return PostSerializers

class PostDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated|ReadOnly]
    lookup_field = "id"

    def get_queryset(self):
        if self.request.user.is_staff:
            return Post.objects.all()
        return Post.objects.filter(approved=True)

    def get_serializer_class(self):
        post_id = self.kwargs['id']
        if self.request.user.is_staff or self.request.user.id == Post.objects.get(id=post_id).author.id:
            return PostOwnerPostSerializers
        return PostSerializers


class CommentListView(ListCreateAPIView):
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