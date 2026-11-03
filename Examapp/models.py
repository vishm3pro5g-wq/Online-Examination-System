
from django.db import models


class Question(models.Model):
    Question = models.CharField(max_length=200)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=100)


class Submission(models.Model):
    student_name = models.CharField(max_length=100)
    question_id = models.IntegerField()
    selected_answer = models.CharField(max_length=100)
    submitted_at = models.DateTimeField(auto_now_add=True)
    point = models.IntegerField(null=True, blank=True)
    remarks = models.TextField(blank=True, default="")
    