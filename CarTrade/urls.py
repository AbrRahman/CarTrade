from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page,name="landing_page"),
    path('home/',views.home,name='home'),
    path('home/<slug:brand_slug>/',views.home,name='car_brand'),
    path('cars/',include('cars.urls'),name='cars'),
    path('profiles/',include('profiles.urls'),name='profiles'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)