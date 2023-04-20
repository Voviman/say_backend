from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='img_blog/')

    def __str__ (self):
        return self.title

