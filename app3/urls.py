from django.urls import path
from app3.views import*
app_name='Deepthi'
urlpatterns = [
    path('page5/',page5,name="page5"),
    path('page6/',page6,name="page6"),
    path('third/',third,name="third"),
]