from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    hire_date = models.DateField(auto_now_add=True)
    experience = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

