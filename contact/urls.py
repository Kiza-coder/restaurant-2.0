from django.urls import path, re_path ##REGULAR_EXPRESSION
from . import views

## Urls calls function in the view and take 2 parameters and 1 optionnal
# 1.A string with the url
# 2.The function called in the views
# 3."name" is a variable who can take the name of the url

urlpatterns = [
	path('',views.contact,name='contact'),
 
]
