from django.db import models

# Create your models here.
class Technical_Skills(models.Model):
    name=models.CharField(max_length=30)

class Tools_and_Technologies(models.Model):
    name=models.CharField(max_length=30)

class Interests(models.Model):
    name=models.CharField(max_length=30)

class Projects(models.Model):
    name=models.CharField(max_length=30)
    details=models.TextField(max_length=200)
    image=models.ImageField(upload_to="projects/")
    live_link=models.URLField(blank=True,null=True)
    github_link=models.URLField(blank=True,null=True)

class Scrollar_Images(models.Model):
    image=models.ImageField(upload_to="Scrollbar_imgs")