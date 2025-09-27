from django.shortcuts import render
from .models import Topic
from .forms import TopicForm, EntryForm
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

def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))
        

    return render(
        request,
        'learning_logs/new_entry.html',
        {'topic': topic, 'form': form}
    )