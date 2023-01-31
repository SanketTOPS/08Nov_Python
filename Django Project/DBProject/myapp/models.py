from django.db import models

# Create your models here.

class usersignup(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    dob=models.DateField()
    mobile=models.IntegerField()
    address=models.TextField()

    def __str__(self) -> str:
        return self.firstname
