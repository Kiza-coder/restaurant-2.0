from django.shortcuts import render

# Function who return a HttpResponse a take in argument :
# 1.The object HttpRequest
# 2.A String with the url of the template
# 3.Variables who can be use in the templates
def delivery(request):
	return render(request, 'delivery/delivery.html', locals()
		)

