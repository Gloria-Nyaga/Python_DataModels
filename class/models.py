from django.db import models

from student.models import Student 

class Class(models.Model):
    class_name = models.CharField(max_length = 20)
    class_capacity = models.PositiveSmallIntegerField ()
    class_duration = models.DateField ()
    students = models.PositiveSmallIntegerField ()
    class_training_assistant = models.CharField(max_length = 20)
    class_representatives = models.TextField ()
    teacher_code = models.PositiveSmallIntegerField ()
    number_of_whiteboards = models.PositiveSmallIntegerField ()
    number_of_TVs = models.PositiveSmallIntegerField ()
    number_of_desks = models.PositiveSmallIntegerField ()
    number_of_chairs = models.PositiveSmallIntegerField ()
    class_code = models.PositiveSmallIntegerField ()
    student=models.ForeignKey(Student, on_delete=models.CASCADE)


