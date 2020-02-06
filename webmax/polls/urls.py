from django.urls import path
from . import views


# Here we define our url paths which link urls to functions in our view page

app_name = 'polls'  # Application namespace for urls -> used to prevent urls overlaps between project apps
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
