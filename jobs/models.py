from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
User = get_user_model()


class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    payment = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    publish_date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length = 100)
    phone_number = models.CharField(max_length = 100)
    employer = models.ForeignKey(User, related_name="employer", on_delete=models.CASCADE)
    employee = models.ForeignKey(User, related_name="employee",on_delete=models.CASCADE, null=True, blank=True)
    employee_queue = models.ManyToManyField(User, related_name="employee_queue", blank=True)

    def __str__(self):
        return self.title

