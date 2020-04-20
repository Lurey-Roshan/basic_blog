from django.db import models

# Create your models here.
class Job(models.Model):
	title=models.CharField(max_length=200)
	date_comp=models.DateTimeField(auto_now_add=True)
	image=models.ImageField(upload_to='job/')
	text=models.TextField(blank=True)

	def  __str__(self):
		return self.title

	def summary(self):
		return self.text[:200]+"....."