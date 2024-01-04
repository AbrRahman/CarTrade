from django.urls import path
from .import views
urlpatterns = [
    path('',views.user_profile,name='profiles'),
    path('register/',views.RegisterClassView.as_view(),name='register'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('edit/',views.profile_edit,name='chang_profile'),
]
