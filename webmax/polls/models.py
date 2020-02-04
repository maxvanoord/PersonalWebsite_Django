from django.db import models

"""
Create your models here.
In our model we define our main data classes which will be transfered to db tables

Update db with models:
   python manage.py makemigrations 'name'      - to make migrations 
   python manage.py migrate                    - to update db with migrations
   
"""

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

