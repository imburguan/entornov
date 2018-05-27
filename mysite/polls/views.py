# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404

#from django.http import HttpResponseRedirect, HttpResponse

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from django.urls import reverse

from django.utils import timezone

from .models import Choice, Question


from django.http import HttpResponse
#from django.template import loader
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

##El siguiente def para el formulario
#@csrf_exempt

##def index(request):
##    #if post request came 
##    if request.method == 'POST':
##        #getting values from post
##        name = request.POST.get('name')
##        email = request.POST.get('email')
##        phone = request.POST.get('phone')
## 
##        #adding the values in a context variable 
##        context = {
##            'name': name,
##            'email': email,
##            'phone': phone
##        }
##        
##        #getting our showdata template
##        template = loader.get_template('prova.html')
##        
##        #returing the template 
##        return HttpResponse(template.render(context, request))
##    else:
##        #if post request is not true 
##        #returing the form template 
##        template = loader.get_template('index.html')
##        return HttpResponse(template.render())
##    #fin de index
#### fin del def para el formulario


class IndexView(generic.ListView):
    
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        context_object_name = 'latest_question_list'
        """Return the last five published questions."""
        for query in Question.objects.order_by('-id')[:50]:
            print(query)
        return Question.objects.order_by('?')[:50]



class Index2View(generic.ListView):
    template_name = 'polls/index2.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        context_object_name = 'latest_question_list'
        """Return the last five published questions."""
        for query in Question.objects.order_by('-id')[:50]:
            print(query)
        return Question.objects.order_by('?')[:50]



class DetailView(generic.DetailView):
    model = Question
    #template_name = 'polls/index2.html'
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


#def vote(request, question_id):
#    ... # same as above


def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
    
