from django.shortcuts import render

from django.shortcuts import render,HttpResponse

from django.views import generic

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

class BookListView(generic.ListView):
	#template=""
	model=Book
	templates="catalog/book_list"
	#queryset=Book.objects.all()[:5]
	context="Book_list"

	def get_queryset(self):
		return Book.objects.all()[:4]



class BookDetailView(generic.DetailView):
	model=Book

class AuthorsListView(generic.ListView):
	model=Author
	#context="authorlist"
	
	'''
	def context_data(self,**kwargs):
		context=super(BookDetailView,self).get_context_data(**kwargs)
	context['some_data']="This is some data"
    '''