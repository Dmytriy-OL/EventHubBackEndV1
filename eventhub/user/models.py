from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)
    surname = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug or Author.objects.filter(pk=self.pk, name=self.name).exists() == False:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
