from django.db import models
from django.urls import reverse, NoReverseMatch


class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=200, blank=True, help_text="Явный URL или name для reverse")
    named_url = models.CharField(max_length=200, blank=True, help_text="Имя url для reverse")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        if self.url:
            return self.url
        return '#'

    def __str__(self):
        return self.title
