
from django.db import models

class Results(models.Model):
    year = models.IntegerField()
    wrote = models.IntegerField()
    passed = models.IntegerField()
    pass_rate = models.FloatField()
    position = models.IntegerField()
    
    def __str__(self):
        return f"Results for {self.year}"

class FAQ(models.Model):
    question = models.CharField()
    answer = models.TextField()
    
    def __str__(self):
        return f"{self.question}?"