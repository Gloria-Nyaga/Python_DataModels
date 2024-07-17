from django.db import models
from student.models import Student

class Teacher(models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    age = models.PositiveSmallIntegerField ()
    teacher_id = models.PositiveSmallIntegerField ()
    email = models.EmailField()
    phone_number = models.CharField ( max_length = 20)
    country = models.CharField(max_length = 20)
    salary = models.PositiveBigIntegerField ()
    specializiation = models.TextField ()
    hire_date = models.DateField ()
    gender = models.CharField(max_length = 10)
    bio = models.TextField ()
    profile_photo = models.ImageField ()
    course_code = models.PositiveSmallIntegerField ()
    student_id=models.ForeignKey(Student, on_delete=models.CASCADE)

# Create your models here.
