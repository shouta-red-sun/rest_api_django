from django.db import models

class Book(models.Model):
    id = models.AutoField(auto_created=True,primary_key=True,editable=False)
    title = models.CharField(max_length=10)
    subtitle = models.CharField(max_length=10)
    author = models.CharField(max_length=10)
    isbn = models.CharField(max_length=13)

    def __str__(self):
        return self.title