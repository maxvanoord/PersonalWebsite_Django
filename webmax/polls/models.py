from django.db import models
from django.utils import timezone
import datetime

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

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # makes an question_id field in db with foreignK
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

