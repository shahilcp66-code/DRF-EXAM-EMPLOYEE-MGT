from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EmpModel(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    department=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    joining_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.department}"


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
        )
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
        )

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=100)
    assigned_to = models.ForeignKey(EmpModel, on_delete=models.CASCADE)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    due_date = models.DateField()

    def __str__(self):
        return self.title

# Create your models here.
