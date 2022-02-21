from django.db import models
from .utils import random_string_generator

# Create your models here
class Url(models.Model):
    origin_url= models.URLField(verbose_name='оригинальй урл',unique=True)
    cut_url = models.CharField(max_length=20,verbose_name='сокращеный урл')
    price = models.IntegerField(default=65)
   
    def save(self, *args, **kwargs):
        if not self.cut_url:
            self.cut_url = random_string_generator()
        super(Url, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return self.cut_url  




