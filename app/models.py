from django.db import models

# Create your models here.
class URLMapping(models.Model):
    long_url = models.URLField()
    short_token = models.CharField(unique=True,db_index=True,max_length=6)
    clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)