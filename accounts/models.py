from django.db import models
from django.contrib.auth.models import User as AuthUser, PermissionsMixin
# Create your models here.


class User(AuthUser, PermissionsMixin):
    pass


