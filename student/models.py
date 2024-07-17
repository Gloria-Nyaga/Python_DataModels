from django.db import models


class Student (models.Model):
    first_name = models.CharField(max_length = 20)
    last_name = models.CharField(max_length = 20)
    student_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField ()
    country = models.CharField(max_length = 20)
    phone_number = models.CharField ( max_length = 20)
    date_of_birth = models.DateField ()
    immediate_kin_contact = models.CharField (max_length = 20)
    county = models.CharField(max_length = 25)
    bio = models.TextField ()
    picture = models.ImageField ()