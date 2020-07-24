from django.db import models

# Create your models here.


class Document(models.Model):
	id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=255, blank=False)
	Email = models.EmailField(max_length=50,null=False,blank=False)
	Message = models.CharField(max_length=255,blank=False)
	File = models.FileField(upload_to='')
	Phone = models.CharField(max_length=10,null=False,blank=False)
	uploaded_at = models.DateTimeField(auto_now_add=True)
