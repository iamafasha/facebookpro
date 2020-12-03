from django.db import models

# Create your models here.
class File(models.Model):
    file = models.FileField(upload_to = './')
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.file.url
    
    