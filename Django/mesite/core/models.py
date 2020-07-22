from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    xlsx = models.FileField(upload_to='books/xlsx/')

    def __str__(self):
        return self.title

    def delete(self,*args, **kwargs):
        self.xlsx.delete()
        super().delete(*args, **kwargs)
