import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    correct_choice = models.ForeignKey("Choice", on_delete=models.CASCADE, related_name='choices', default=1)
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def is_choice_correct(self, choice_id):
        return self.choice_set.filter(id=choice_id, is_correct=True).exists()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
    
chose = models.BooleanField(default=False)

# Create your models here.
