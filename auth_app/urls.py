
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('dashboard/',views.dashboard_view,name='dashboard'),
    path('forget-password/',views.forgetpassword_view, name='forget_password'),

]