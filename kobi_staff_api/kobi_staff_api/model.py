from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class StaffBase(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"

class Manager(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resumes')
    department = models.CharField(max_length=255)
    has_company_card = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

class Intern(models.Model):
    company_name=models.CharField(max_length=255)
    industry = models.CharField(max_length=255)
    company_email = models.EmailField(unique = True)
    company_phonenumber = models.CharField(max_length =20)
    company_address = models.ForeignKey(Address, on_delete = models.CASCADE)


class CustomUser(AbstractUser):
    address = models.OneToOneField(Address, on_delete=models.CASCADE, related_name='user_address', null=True, blank=True)
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name='user_resume', null=True, blank=True)
   