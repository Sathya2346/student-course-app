from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    duration = models.CharField(max_length=50)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title


class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)