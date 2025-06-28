from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.



class StaffBase(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    poster_code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"

class Manager(models.Model):
    # user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='resumes')
    name = models.CharField(max_length=255)
    department = models.TextField()
    experience = models.TextField()
    education = models.TextField()
    skills = models.TextField()
    has_company_card = models.BooleanField()
    apprentice = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class Intern(models.Model):
    Intern_name=models.CharField(max_length=255)
    Workfield = models.CharField(max_length=255)
    Experience = models.EmailField(unique = True)
    Intern_phonenumber = models.CharField(max_length =20)
    Intern_address = models.ForeignKey(StaffBase, on_delete = models.CASCADE)
    Mentor = models.TextField()
    Internship_end = models.DateTimeField()

    def __str__(self):
        return f"{self.Intern_name},{self.Experience},{self.Mentor}"
    
class Address(models.Model):
    user = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='addresses')
    user = models.ForeignKey(Intern, on_delete=models.CASCADE, related_name='addresses')
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    poster_code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.state}, {self.country}"



