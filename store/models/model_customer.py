from django.db import models

class Customer(models.Model):
    GENDER_CHOICE = [  
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHERS', 'Others'),
    ]
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50,)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=500)
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
