from django.shortcuts import render
from .forms import ContactForm

# Function who return a HttpResponse a take in argument :
# 1.The object HttpRequest
# 2.A String with the url of the template
# 3.Variables who can be use in the templates
def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		name = form.cleaned_data['name']
		firstname = form.cleaned_data['firstname']
		gender = form.cleaned_data['gender']
		message = form.cleaned_data['message']
		envoi = True
		form.save()
		return render(request, 'contact/contact_valid.html', locals()
		)
	return render(request, 'contact/contact.html', locals()
	)






