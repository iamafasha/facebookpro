from rest_framework.serializers import ModelSerializer
from post.models import Post , Comment ,PostMedia, PostLike

class PostSerializers(ModelSerializer):
    
    class Meta:
        model= Post
        fields = ['id','text','author', 'approved','created_date']