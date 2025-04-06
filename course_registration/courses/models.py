from django.db import models
import uuid
from accounts.models import *
# Create your models here.
class Course(models.Model):
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255,unique=True)
    faculty = models.ForeignKey(Faculty, related_name='courses',on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Registration(models.Model):
    status_choices = (
        ('Pending','Pending'),
        ('Completed','Completed')
        )
    
    student = models.ForeignKey(Student,related_name='courses',on_delete=models.CASCADE)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    status = models.CharField(max_length=50, default='Pending',choices=status_choices)

    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('student','course')

    def __str__(self):
        return f'{self.student.name} - {self.course.name}'