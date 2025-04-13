from django.db import models

class CppExample(models.Model):
    code = models.TextField()
    status = models.CharField(max_length=100)
    explanation = models.TextField()

    def __str__(self):
        return f"Example #{self.id}"
