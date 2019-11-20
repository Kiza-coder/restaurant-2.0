from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', include('home.urls')),
    path('menu/', include('menu.urls')),
    path('story/', include('story.urls')),
    path('contact/', include('contact.urls')),
    path('delivery/', include('delivery.urls')),
    path('gallery/', include('gallery.urls')),


]
