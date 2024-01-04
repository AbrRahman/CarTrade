from django.db import models
from django.contrib.auth.models import User
from cars.models import CarModel
# Create your models here.
class OrderModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='order')
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='order')
    quantity=models.IntegerField(null=True)

    def __str__(self) -> str:
        return f"User : {self.user} Cars : {self.car}"