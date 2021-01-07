from django.db import models


# Create your models here.

class scrapdata(models.Model):
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    release_date = models.CharField(max_length=10)
    duration = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
