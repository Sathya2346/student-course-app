from django.shortcuts import render, get_object_or_404
from .models import Course

def dashboard(request):
    courses = Course.objects.all()
    return render(request, 'dashboard.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_detail.html', {'course': course})