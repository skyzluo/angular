from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context = {'latest_question_list': "dd"}
    return render(request, 'polls/index.html', context)