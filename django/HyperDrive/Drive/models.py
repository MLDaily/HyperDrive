from django.db import models

# Create your models here.

class UserInfo(models.Model):
	uid = models.IntegerField(default=1,primary_key=True)
	uname = models.CharField(max_length=200, default=None)
	upass = models.CharField(max_length=200)

class Places(models.Model):
	pid = models.IntegerField(null=False, primary_key=True)
	pname = models.CharField(max_length=200, default=None)
	plat = models.FloatField(default=None)
	plon = models.FloatField(default=None)
	ptype = models.CharField(max_length=200, default=None)
	ploc = models.CharField(max_length=200, default=None)

class UserPlaces(models.Model):
	userid = models.ForeignKey(UserInfo, related_name='userid',null=False)
	placeid = models.ForeignKey(Places, related_name='placeid',null=False)

