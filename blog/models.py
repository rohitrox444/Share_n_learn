from django.db import models

# Create your models here.

class blog_list(models.Model):

    blog_name = models.CharField(max_length=100)
    blog_description = models.CharField(max_length=100)
    

    class Meta:
        db_table = "blog_list"
