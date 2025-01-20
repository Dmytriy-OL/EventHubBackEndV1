from django.db import models
from django.urls import reverse


class Event(models.Model):
    name = models.CharField(max_length=50)
    authorId = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('EventCategory', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_event', kwargs={'event_id': self.pk})


class EventCategory(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'category_id': self.pk})
