from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    deadline = models.DateField(null=True, blank=True)
    priority = models.CharField( max_length=5)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.title