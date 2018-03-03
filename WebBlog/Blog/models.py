from django.db import models
import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    Describ = models.TextField()
    date = models.DateField(default=datetime.date.today)


    def __str__(self):
        return self.title
