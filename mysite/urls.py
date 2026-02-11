from . import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import home, contact, check_otp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('check/', check_otp, name='check'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
