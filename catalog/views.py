from django.shortcuts import render

from django.shortcuts import render,HttpResponse

from . models import Book,BookInstance, Author, Genre

# Create your views here.

def index(request):
	#no of books and objects
	num_books=Book.objects.all().count()
	num_Instances=BookInstance.objects.all().count()

	#No of books available
	num_instance_available=BookInstance.objects.filter(status="a").count()
	num_authors=Author.objects.all().count()


	context={
	"num_books":num_books,
	"num_Instances":num_Instances,
	"num_instance_available":num_instance_available,
	"num_authors":num_authors,
	}

	return render(request,"catalog/index.html",context)



