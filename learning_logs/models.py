from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, related_name='entries')
    created_date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        verbose_name = 'Entry'
        verbose_name_plural = 'Entries'

    def __str__(self):
        return self.text[:50]+'...'