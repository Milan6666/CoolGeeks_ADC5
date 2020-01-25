from django.db import models

# Create your models here.
class food(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="food/files")

    def __str__(self):
        return self.title