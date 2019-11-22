from django.shortcuts import render

# Create your views here.
def menu(request):
	return render(request, 'menu/menu.html',locals()
		)

def menu_burger(request):
	return render(request, 'menu/menu_burger.html', locals()
		)