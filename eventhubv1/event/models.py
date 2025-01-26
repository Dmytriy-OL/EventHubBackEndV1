from django.db import models
from django.urls import reverse


class Event(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Url")
    authorId = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=False)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('EventCategory', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_event', kwargs={'event_slug': self.slug})

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'All Events'
        ordering = ['data', 'name']


class EventCategory(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Url")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        # ordering = ['-name']
