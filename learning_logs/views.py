from django.shortcuts import render
from .models import Topic

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
