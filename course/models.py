from django.db import models
from student.models import Student

class Course(models.Model):
    course_title = models.CharField(max_length = 20)
    course_category = models.TextField ()
    course_start_date = models.DateField ()
    course_end_date = models.DateField ()
    course_code = models.PositiveSmallIntegerField ()
    teacher_code = models.PositiveSmallIntegerField ()
    student_code = models.PositiveSmallIntegerField ()
    student_number = models.PositiveSmallIntegerField ()
    course_fee = models.PositiveSmallIntegerField ()
    student=models.ForeignKey(Student, on_delete=models.CASCADE)


