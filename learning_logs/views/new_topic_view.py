from django.shortcuts import render
from learning_logs.forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    return render(
        request,
        'learning_logs/new_topic.html',
        {'form': form}
    )