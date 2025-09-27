from django.shortcuts import render
from.models import Topic
from.forms import TopicForm
from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
    return render(
        request,
        'learning_logs/index.html'
    )

def topics(request):
    topics = Topic.objects.order_by()
    
    return render(
        request,
        'learning_logs/topics.html',
        {'topics': topics}
    )

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entries.order_by('-created_date') # type: ignore

    return render(
        request,
        'learning_logs/topic.html',
        {'topic': topic, 'entries': entries,}
    )

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