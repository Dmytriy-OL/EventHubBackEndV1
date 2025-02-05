from PIL import Image
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    nickname = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    surname = models.CharField(max_length=50, blank=True)
    avatar = models.ImageField(upload_to='images/%Y/%m/%d', blank=True)
    banner = models.ImageField(upload_to='banners/', blank=True)

    def __str__(self):
        return self.nickname

    # def clean(self):
    #     super().clean()
    #     if self.banner:
    #         img = Image.open(self.banner)
    #         if img.width != 1200 or img.height != 400:
    #             raise ValidationError("Зображення має бути розміром 1200x400 пікселів.")

    def save(self, *args, **kwargs):
        if not self.slug or Author.objects.filter(pk=self.pk, name=self.nickname).exists() == False:
            self.slug = slugify(self.nickname)
        super().save(*args, **kwargs)
