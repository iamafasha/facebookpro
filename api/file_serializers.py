from rest_framework import serializers
from files.models import File

class FileSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = File
        fields =['file']