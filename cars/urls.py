from django.urls import path
from .import views
urlpatterns = [
    # path('<int:id>/',views.car_details,name='car_details'),
    path('<int:id>/',views.CarDetailsView.as_view(),name='car_details'),
    path('buyproduct/<int:id>/',views.buy_product,name='buy_product'),
]
