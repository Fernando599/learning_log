from django.shortcuts import render
from learning_logs.models import Topic
from learning_logs.forms import EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse

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