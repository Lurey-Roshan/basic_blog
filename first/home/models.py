from django.db import models

# Create your models here.
class Home(models.Model):
	greeting=models.TextField()
	email=models.EmailField(max_length=50)
	profile_pic=models.ImageField(upload_to='profile_pic/')
	contact=models.IntegerField(blank=True,null=True)
