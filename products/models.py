from django.db import models
from django.contrib.auth.models import User

# Product Class

# url
# votes_total
# image
# icon 
# body

#pub_date_pretty

# hunter

class Product(models.Model):
	title = models.CharField(max_length=100)
	url = models.TextField(max_length=200)
	body = models.TextField(max_length=500)
	pub_date = models.DateTimeField()
	votes_total = models.IntegerField(default=1)
	image = models.ImageField(upload_to = 'images/')
	icon = models.ImageField(upload_to = 'images/')

	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		 return self.title

	def summary(self):
		return self.body[:100]

	def pub_date_pretty(self):
		return self.pub_date.strftime('%b %e %Y')




