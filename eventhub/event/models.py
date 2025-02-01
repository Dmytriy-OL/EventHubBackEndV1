from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from pytils.translit import translify


class Event(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Url", blank=True)
    authorId = models.ForeignKey('user.Author', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d', blank=False)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or Event.objects.filter(pk=self.pk, name=self.name).exists() == False:
            self.slug = slugify(translify(self.name))  # Транслітерація + slugify
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('show_event', kwargs={'event_slug': self.slug})

    def get_edit_url(self):
        return reverse("edit_event", kwargs={'event_slug': self.slug})

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'All Events'
        ordering = ['data', 'name']


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Url")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('show_category', kwargs={'category_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        # ordering = ['-name']


