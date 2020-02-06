from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question, Choice

# Create your views here.
# Parameter 'request' is always needed in a view. other parameters are arguments that are passed by in urls

# Each view is responsible for returning a HttpsResponse(page content) or an error 


def index(request):
    latest_question_list = Question.objects.all() # Loading data from the database 
    
    template = loader.get_template('polls/index.html') # Loading the html template for this page into a variable

    context = { # In context we pass a dict with the data we need to show in our html page
        'latest_question_list' : latest_question_list
    }

    return HttpResponse(template.render(context, request))  # Rendering the template with it's passed data variables


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    
    context = {'question' : question}

    return render(request, 'polls/detail.html', context)    # We can also call render with the page reference in it directly


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of question {question_id}.")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")
