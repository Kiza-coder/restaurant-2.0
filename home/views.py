from django.shortcuts import render, get_object_or_404, get_list_or_404
from home.models import Event, Promotion

# Function who return a HttpResponse a take in argument :
# 1.The object HttpRequest
# 2.A String with the url of the template
# 3.Variables who can be use in the templates
def home(request):
	events = get_list_or_404(Event)
	promotions = get_list_or_404(Promotion)
	return render(request, 'home/home.html', {'events':events,'promotions':promotions }
		)

