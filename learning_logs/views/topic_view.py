from django.shortcuts import render
from learning_logs.models import Topic

def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entries.order_by('-created_date') # type: ignore

    return render(
        request,
        'learning_logs/topic.html',
        {'topic': topic, 'entries': entries,}
    )