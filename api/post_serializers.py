from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from post.models import Post, Comment, PostMedia, PostLike

class PostLikeSerializers(ModelSerializer):
    class Meta:
        model = PostLike
        fields = ['id', 'post', 'author']

class PostCommentsListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        user =  self.context['request'].user
        new_data = data
        if hasattr(data, 'first'):
            post_author_id = data.first().reply_to.author.id
        # if not athenticated need to only approved
        # if owner of post needs to see all posts including un approved
        # if not owner need to see both approved and unapproved which you own
        # if super user then show all
            if not user.is_authenticated:
                print('not authenticated')
                new_data = data.filter(approved=True)
            else:
                if post_author_id == user.id:
                    new_data=data
                else:
                    print("looking for owned comments")
                    user_data = data.filter(author = user)
                    new_data = user_data|data.filter(approved=True)
        new_data =new_data.order_by("-created_date")
        return super(PostCommentsListSerializer, self).to_representation(new_data)

class PostMediaSerializers(ModelSerializer):
    class Meta:
        model = PostMedia
        fields = ['id', 'image']

class PostCommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text', 'author' , 'approved' , 'created_date']
        read_only_fields = ['author', 'approved' ,'created_date']
        list_serializer_class = PostCommentsListSerializer
        
class PostOwnerPostComentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text', 'author', 'approved','created_date']
        read_only_fields = ['author', 'created_date']
        list_serializer_class = PostCommentsListSerializer


class CommentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text', 'author' , 'approved' , 'created_date']
        read_only_fields = ['author', 'approved' ,'created_date']
        
class PostOwnerComentSerializers(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','text', 'author', 'approved','created_date']
        read_only_fields = ['author', 'created_date']


class PostSerializers(ModelSerializer):
    likes_count = serializers.SerializerMethodField(read_only=True)
    comments = PostCommentSerializers(source='comment_set', many=True, read_only=True)
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

class PostOwnerPostSerializers(PostOwnerComentSerializers):
    likes_count = serializers.SerializerMethodField(read_only=True)
    post_media = PostMediaSerializers(source='postmedia_set', many=True, required=False)
    comments = PostOwnerPostComentSerializers(source='comment_set', many=True, read_only=True)
    class Meta:
        model = Post
        fields = [
            'id', 'text', 'likes_count', 'likes_count',
            'post_media', 'author', 'approved', 'comments','created_date',
        ]
        read_only_fields = ['author', 'approved', 'comments','created_date',]
    def get_likes_count(self, obj):
        return obj.postlike_set.count()
