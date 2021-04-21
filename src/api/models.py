from django.db import models


class RequestEntity(models.Model):
    requestTime = models.DateTimeField(auto_now=True)
    gridSize = models.IntegerField()
    gridStructure = models.TextField()
