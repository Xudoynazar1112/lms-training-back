from django.contrib.auth.models import AbstractUser
from django.db import models

ADMIN, TEACHER, STUDENT = ('admin', 'teacher', 'student')


class CustomUser(AbstractUser):
    USER_ROLES = (
        (ADMIN, ADMIN),
        (TEACHER, TEACHER),
        (STUDENT, STUDENT),
    )
    user_roles = models.CharField(max_length=31, choices=USER_ROLES, default=STUDENT)
    photo = models.ImageField(upload_to='photos/', default='photos/default.jpg')
    phone_number = models.IntegerField(null=True, blank=True)
