from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    Describ = models.TextField()
    data = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
