from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.urls import reverse

# Create your models here.

class admitpasent(models.Model):
	name=models.CharField(max_length=20)
	gender=models.CharField(max_length=10)
	birthdate=models.DateTimeField(default=timezone.now)
	address=models.CharField(max_length=60)
	diseases=models.CharField(max_length=10)
	admit_date=models.DateTimeField(default=timezone.now)
	admit_charge=models.CharField(max_length=30)
	user =models.ForeignKey(User,on_delete=models.CASCADE)

	def get_absolute_url(self):
		return reverse('patientdetail')

	def __str__(self):
		return f'Patiant name => {self.name}, And admit_date => {self.admit_date}'

class userprofile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	pimg = models.ImageField(default='default.jpg', upload_to='profile_pic')
	

	def __str__(self):
		return f'User name is => {self.user.username}, And Profile_Pic name is => {self.pimg}'

	def save(self):
		super().save()
		img = Image.open(self.pimg.path)
		if img.height>300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.pimg.path)
	

