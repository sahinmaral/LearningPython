from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, verbose_name="Film Name")
    description = models.TextField(verbose_name="Film Description")
    image = models.CharField(max_length=50, verbose_name="Film Image")
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Film Created Date")
    isPublished = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def get_image_path(self):
        return "img/" + self.image
