from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Visitor(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	phone_no = models.CharField(max_length = 10)
	address = models.TextField(max_length=200)

	def __str__(self):
		return self.user.first_name


class Room(models.Model):
	visitor = models.ManyToManyField(Visitor,through= 'Booking')
	room_no =  models.CharField(max_length=4)
	location = models.CharField(max_length=4)
	facilities = models.CharField(max_length=50)

	def __str__(self):
		return self.room_no +' --> '+self.location


class Booking(models.Model):

	visitor = models.ForeignKey(Visitor,models.SET_NULL, blank=True, null=True)
	room = models.ForeignKey(Room,on_delete=models.CASCADE)
	from_date = models.DateField(auto_now=False,auto_now_add =False)
	to_date = models.DateField(auto_now=False,auto_now_add =False)
