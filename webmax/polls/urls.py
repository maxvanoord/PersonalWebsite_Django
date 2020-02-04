from django.urls import path
from . import views


# Here we define our url paths which link urls to functions in our view page

urlpatterns = [
    path('', views.index, name='index')
]
