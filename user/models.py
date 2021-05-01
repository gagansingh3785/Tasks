from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class CustomAccountManager(BaseUserManager):

	def create_user(self, email, password, user_type, **other_fields):

		if not email:
   			raise ValueError('Users must have an email address')

		email = self.normalize_email(email)
		user = self.model(email=email, user_type=user_type, password=None)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, password, user_type, **other_fields):
		print("creating a super user")

		user = self.create_user(email, password, user_type, **other_fields)
		user.is_staff = True
		user.is_active = True
		user.is_superuser = True
		user.save()
		print(user.is_staff)
		print(user.is_superuser)
		return user


class NewUser(AbstractBaseUser, PermissionsMixin):
	user_choice = [('M', "manager"), ('C', "customer")]
	user_type = models.CharField(max_length=1, choices=user_choice)
	email = models.EmailField(unique=True)
	
	is_staff = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['user_type']

	objects = CustomAccountManager()

	def __str__(self):
		return self.email
