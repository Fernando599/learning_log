from django.shortcuts import render
from learning_logs.models import Topic

def topics(request):
    topics = Topic.objects.order_by()
    
    return render(
        request,
        'learning_logs/topics.html',
        {'topics': topics}
    )