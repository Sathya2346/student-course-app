from django.urls import path
from .views import dashboard
from . import views

urlpatterns = [
    path('', dashboard, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
]