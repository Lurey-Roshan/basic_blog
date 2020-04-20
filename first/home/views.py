from django.shortcuts import render
from home.models import Home
# Create your views here.
def home(request):
	hom=Home.objects.all()
	context = {
		'home':hom
		}

	return render(request,'home/home.html',context)