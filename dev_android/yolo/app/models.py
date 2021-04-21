from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(blank=True, null=True)
    text = models.TextField()

    def __str__(self):
        return self.postname




