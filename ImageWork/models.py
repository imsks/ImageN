from django.db import models


class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    mined_text = models.CharField(max_length=500, null=True, default="Start server again to mine. still shows error then can't mine")

    def __str__(self):
        return self.title
