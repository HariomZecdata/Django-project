# myproject/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', include('myapp.urls')),  # Include the URLs from 'myapp'
]
