from django.contrib import admin
from .models import Url

# Register your models here.
@admin.register(Url)
class UrlAdmin(admin.ModelAdmin):
   list_display = ['cut_url' , 'origin_url']