from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import ImageUrl

# Function who return a HttpResponse a take in argument :
# 1.The object HttpRequest
# 2.A String with the url of the template
# 3.Variables who can be use in the templates
def gallery(request):
	images = ImageUrl.objects.order_by('order')
	images_list1 = [images[0],images[1],images[2]]
	images_list2 = [images[3],images[4],images[5]]
	images_list3 = [images[6],images[7],images[8]]
	images_list = [images_list1, images_list2, images_list3]
	return render(request, 'gallery/gallery.html', {'images_list':images_list }
		)
	

