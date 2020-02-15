from django.db import models


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    mined_text = models.CharField(max_length=500, null=True, default='')

    def __str__(self):
        return self.title
