import secrets
import string

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

    def generate_password(self):
        return ''.join(secrets.choice(string.digits) for _ in range(8))

    def generate_username(self):
        return ''.join(secrets.choice(string.ascii_letters) for _ in range(6))

    def save(self, *args, **kwargs):
        if not self.username:  # Only generate if the username is not provided
            self.username = self.generate_username()

        if not self.pk:  # Only generate a password for new users
            raw_password = self.generate_password()
            self.set_password(raw_password)
            # You can print the password for now or log it somewhere securely
            print(f"Generated password for user {self.username}: {raw_password}")

        super().save(*args, **kwargs)
