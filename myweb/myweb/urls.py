
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('base.urls')),
    path('about/', include('base.urls')),
    path('contact/', include('base.urls'))

]
