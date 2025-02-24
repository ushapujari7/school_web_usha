from django.contrib import admin
from django.urls import path,include
from .views import home_view  # Import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),  # Home page URL
    path('teachers',include('teachers.urls')),
    path('students', include('students.urls')),
]
