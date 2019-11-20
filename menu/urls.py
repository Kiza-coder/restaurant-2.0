from django.urls import path, re_path ##REGULAR_EXPRESSION
from . import views


urlpatterns = [
	path('',views.menu,name='menu'),
 
]
