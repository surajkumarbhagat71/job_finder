from django.db import models
from django.contrib.auth.models import User
from django.conf import settings



class CompanyeeDetails(models.Model):
    com_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    com_name = models.CharField(max_length=200)
    com_email = models.EmailField()
    com_logo = models.ImageField(upload_to = 'media/')
    com_city = models.CharField(max_length=200)
    com_address = models.CharField(max_length=200)

    def __str__(self):
        return self.com_name


class Jobs(models.Model):
    job_id = models.AutoField(primary_key=True)
    com_id = models.ForeignKey(CompanyeeDetails,on_delete=models.CASCADE)
    job_name = models.CharField(max_length=200)
    exprience = models.CharField(max_length=300)
    edication = models.CharField(max_length=400)
    job_type = models.CharField(max_length=200)
    schedule = models.CharField(max_length=200)
    salary = models.IntegerField()
    dicription = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.job_name


class Apply(models.Model):
    apply_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Jobs,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    resume = models.FileField(upload_to='media/')
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default = False)

    def __str__(self):
        return self.first_name



