from django.urls import path, include
from . import views

urlpatterns = [
    path('skills/',views.skills, name="skillsPage"),
]