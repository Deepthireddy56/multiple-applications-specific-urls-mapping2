from django.urls import path
from app1.views import*
app_name='Something'
urlpatterns = [
    path('page1/',page1,name="page1"),
    path('page2/',page2,name="page2"),
    path('first/',first,name="first"),
]