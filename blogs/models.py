from django.db import models

class Blog(models.Model):
	title = models.CharField(max_length=100)
	pub_date = models.CharField(max_length=20)
	body = models.CharField(max_length=200)
	image = models.ImageField(upload_to='images/')
