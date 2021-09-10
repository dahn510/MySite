from django.db import models
from django.utils import timezone

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # Return human readable representation of this model
    def __str__(self):
        return self.title

