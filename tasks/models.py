from django.db import models
from user.models import NewUser
# Create your models here.

class Task(models.Model):
	choices = [('C', "Completed"), ('P', "Pending")]
	name = models.CharField(max_length=200)
	creator = models.ForeignKey(NewUser, related_name="creator", on_delete=models.CASCADE)
	moderator = models.ForeignKey(NewUser, related_name="moderator", on_delete=models.RESTRICT)
	status = models.CharField(max_length=1, choices=choices)
	description = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Notifications(models.Model):
	title = models.CharField(max_length=200)
	user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
	read = models.BooleanField(default=False)

	def __str__(self):
		return self.title