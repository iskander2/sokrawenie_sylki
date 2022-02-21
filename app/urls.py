
from django.urls import path
from .views import UrlListView,UrlCreatView, redirect_1,ololo,search

app_name = "app"
urlpatterns = [
    path('urls/' , UrlListView.as_view(), name = 'urls'),
    path('create/' ,UrlCreatView.as_view(), name ='create'),
    path('search/',search, name ='search' ),
    path('' ,ololo,name='ololo' ),
    path('<str:cut_url>/' ,redirect_1, name='redirect_1' ),


]
