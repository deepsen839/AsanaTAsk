from django.db import models

# Create your models here.
class asanaModel(models.Model):
 taskname = models.CharField(max_length = 200)
 notes = models.CharField(max_length = 200)
 task_id = models.IntegerField(null = True)