from django.db import models
class BrandModel(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=120)
    def __str__(self) -> str:
        return self.name

class CarModel(models.Model):
    image=models.ImageField(upload_to ='uploads/')
    name=models.CharField(max_length=100)
    description=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    brand=models.ForeignKey(BrandModel,on_delete=models.CASCADE,related_name="car_model")
    
    def __str__(self) -> str:
        return self.name

class CommentModel(models.Model):
    name=models.CharField(max_length=100)
    comment_body=models.TextField()
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name="comment")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
