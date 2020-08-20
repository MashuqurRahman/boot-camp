from django.db import models
from taggit.managers import TaggableManager
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=250)
    content=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    tags=TaggableManager()

    class Meta:
        ordering = ('-created',)
    def __str__(self):
        return self.title