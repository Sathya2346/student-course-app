from django.urls import path
from .views import dashboard
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', dashboard, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('course/<int:id>/', views.course_detail, name='course_detail'),
]

# ADD THIS AFTER urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)