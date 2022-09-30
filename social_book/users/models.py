from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
from datetime import date

class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    mobile = models.CharField(max_length=10)
    public_visibility = models.BooleanField(default=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=254, null=True, blank=True)
    roles = {('author', 'Author'),
             ('seller', 'Seller')}
    roles = models.CharField(max_length=10, choices=roles, default='seller')

    objects: UserManager

    @property
    def age(self):
        if (self.birth_date != None):
            age = date.today().year - self.birth_date
            return int((age))
