from django.shortcuts import render
from .models import Course

def dashboard(request):
    courses = Course.objects.all()
    return render(request, 'dashboard.html', {'courses': courses})