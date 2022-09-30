from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations: True

def create_user(self, email, password=None, **extra_field):

    if not email:
        raise ValueError('Email is required ')
    
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_field)
    user.set_password(password)
    user.save(using=self.db)
    user.save()
    return user

def create_superuser(self, email, password=None, **extra_field):

    extra_field.setdefault('is_staff', True)
    extra_field.setdefault('is_superuser', True)
    extra_field.setdefault('is_staff', True)

    if extra_field.get('is_staff') is not True:
        raise ValueError(('Super user must have is_Staff is True'))

    return self.create_user(email, password, **extra_field)