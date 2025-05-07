from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    
        gender_choices=[('M','Мужской'),('F','Женский')]

        gender=models.CharField(
            max_length=1,
            choices=gender_choices,
            verbose_name='Пол',
            blank=False,
            null=False
        )

    
    
    
    

# Create your models here.
