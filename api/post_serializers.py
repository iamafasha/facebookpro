from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from post.models import Post, Comment, PostMedia, PostLike


class PostMediaSerializers(ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['id', 'image']


class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text', 'author', 'created_date']
        read_only_fields = ['author', 'created_date']


class PostSerializers(ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)
    comments = CommentSerializers(source='comment_set', many=True, read_only=True)
    post_media = PostMediaSerializers(source='postmedia_set', many=True, required=False)

    class Meta:
        model = Post
        fields = [
            'id', 'text', 'likes_count', 'likes_count',
            'post_media', 'author', 'approved', 'comments','created_date',
        ]
        read_only_fields = ['author', 'approved', 'comments','created_date',]

    def get_likes_count(self, obj):
        return obj.postlike_set.count()

    def create(self,validated_data):
        user =  self.context['request'].user
        instance=Post.objects.create(author=user ,**validated_data)
        return instance


class PostLikeSerializers(ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'author']
