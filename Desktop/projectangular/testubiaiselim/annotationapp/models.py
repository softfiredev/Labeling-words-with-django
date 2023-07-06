from django.db import models

# Create your models here.
class Annotation(models.Model):
    document = models.TextField()
    start_position = models.PositiveIntegerField()
    end_position = models.PositiveIntegerField()
    label = models.CharField(max_length=255)
    annotated_text = models.TextField()