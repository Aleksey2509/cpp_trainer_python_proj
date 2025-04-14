"""Models for app"""
from django.db import models
from django.contrib.auth.models import User

class CppExample(models.Model):
    """Cpp example model"""
    code = models.TextField()
    status = models.CharField(max_length=100)
    explanation = models.TextField()

    def __str__(self):
        return f"Example #{self.id}"


class QuizAttempt(models.Model):
    """quiz attempt model (for tracking user score)"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cpp_example = models.ForeignKey(CppExample, on_delete=models.CASCADE)
    is_correct = models.BooleanField()
    submitted_at = models.DateTimeField(auto_now_add=True)
