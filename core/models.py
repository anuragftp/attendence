from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.functions import ExtractMonth
# Create your models here.


User = get_user_model()


LEAVE_CHOICES=[
	('SL','Sick-Leave'),
	('ML','Maternity Leave'),
]

STATUS_CHOICES=[
	('Pending','Pending'),
	('Approved','Approved'),
	('Reject','Reject'),
]

class Attendence(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	check_in = models.TimeField(auto_now_add=True)
	check_out = models.TimeField(auto_now=True)
	working_hours=models.FloatField(default=0)
	date=models.DateField(auto_now_add=True)

	def __str__(self):
		return self.user.full_name

class Leave(models.Model):
	leave_type=models.CharField(max_length=100, choices=LEAVE_CHOICES,null=True,blank=True)
	state = models.CharField(max_length=50, choices=STATUS_CHOICES, null=True, blank=True)
	reason = models.CharField(max_length=200)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	maxleave = models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_on']
		
	def __str__(self):
		return self.user.full_name


class AnnualLeave(models.Model):
	holiday_name = models.CharField(max_length=100)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	month=models.IntegerField()
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['-created_on']

	def __str__(self):
		return self.holiday_name