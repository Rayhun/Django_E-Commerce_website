from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    GENDER_CHOICE = [  
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHERS', 'Others'),
    ]
    user = models.OneToOneField(User, null=True,blank=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50, null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True,default="demo.jpg")
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=500)
    bio = models.TextField(null=True, blank=True)
    birth_day = models.CharField(null=True, blank=True,max_length=200)
    gender = models.CharField(
        max_length=6,
        choices = GENDER_CHOICE,
        default='MALE',
        null=True,
    )

    def __str__(self):
        return self.username

    @staticmethod
    def get_customer_by_username(username):
        try:
            return Customer.objects.get(username=username)
        except:
            return False

    def register(self):
        self.save()
