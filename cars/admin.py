from django.contrib import admin
from cars.models import CarModel,BrandModel,CommentModel
class BrandAdmin(admin.ModelAdmin):
   prepopulated_fields={"slug":("name",)}
   list_display=['name','slug']

admin.site.register(BrandModel,BrandAdmin)
admin.site.register(CarModel)
admin.site.register(CommentModel)
