from django.db import models


class News(models.Model):
    title = models.CharField(max_length=128, unique=True)
    author = models.CharField(max_length=128)
    date = models.DateField()
    description = models.CharField(max_length=10000)


    class Meta:
        verbose_name_plural = 'News'

    def __str__(self):
        return self.title
