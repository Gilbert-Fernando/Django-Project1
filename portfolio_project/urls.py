from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('directive/', include('directive.urls')),
    path('template1/', include('template1_app.urls')),
    path('template2/', include('template2_app.urls')),
    path('template3/', include('template3_app.urls')),
]