from __future__ import unicode_literals

from django.db import models

# Create your models here.
class blogPost(models.Model):
	title=models.CharField(max_length=255)
	short_description=models.TextField()
	content=models.TextField()
	image=models.FileField(upload_to="")
	created_at=models.DateTimeField()
	posted_by=models.CharField(max_length=150)
	order=models.IntegerField(default=0)

	class Meta:
		ordering = ['-order',]
	
	def __str__(self):
		return self.title
blogPost.allow_tags = True
#class feedback(models.Model):
#	name=models.CharField(max_length=150)
#	email=models.EmailField()
#	subject=models.CharField(max_length=150)
#	body=models.TextField()