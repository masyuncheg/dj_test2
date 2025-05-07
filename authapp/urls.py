from django.urls import path
from . import views
urlpatterns = [
path('log/', views.log_view, name='login'),
path('reg/', views.reg_view, name='register'),
]