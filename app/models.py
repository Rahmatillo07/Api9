from django.core.validators import FileExtensionValidator
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=20,verbose_name='nomi')
    video = models.FileField(upload_to='video',validators=[
        FileExtensionValidator(allowed_extensions=['mp4','MOV','AVI','WMV'])
    ])

    class Meta:
        unique_together = ['title']

    def __str__(self):
        return self.title



