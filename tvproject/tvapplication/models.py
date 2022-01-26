from django.db import models

# Create your models here.
class tv(models.Model):
    model_no=models.IntegerField()
    tv_name=models.CharField(max_length=50)
    type=models.CharField(max_length=50)
    features=models.CharField(max_length=100)


    color=models.CharField(max_length=50)
    price=models.IntegerField()
    rack=models.IntegerField(default=0)
    stock=models.IntegerField(default=0)
