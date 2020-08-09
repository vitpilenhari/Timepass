from django.db import models

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.TextField(max_length=10)
    content=models.TextField()
    desc=models.CharField(max_length=300,default="")
    slug=models.CharField(max_length=100)
    time=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
class Contact(models.Model):
    sno=models.AutoField(primary_key=True)
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    phone=models.CharField(max_length=12)
    feedback=models.TextField()
    time=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
