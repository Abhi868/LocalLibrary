
from datetime import date

from django.shortcuts import render

from django.shortcuts import render,HttpResponse,get_object_or_404,reverse

from django.views import generic

from . models import Book,BookInstance, Author, Genre
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
	model="BookInstance"
	template_name="catalog/bookinstance_list_borrowed_user.html"
	paginate_by=2
	
	def get_queryset(self):
		return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact="o").order_by("due_back")


def index(request):
	#no of books and objects
	num_books=Book.objects.all().count()
	num_Instances=BookInstance.objects.all().count()

	#No of books available
	num_instance_available=BookInstance.objects.filter(status="a").count()
	num_authors=Author.objects.all().count()
	num_visits=request.session.get('num_visits',0)
	request.session['num_visits']=num_visits+1
	context={
	"num_books":num_books,
	"num_Instances":num_Instances,
	"num_instance_available":num_instance_available,
	"num_authors":num_authors,
	"num_visits":num_visits,
	}

	return render(request,"catalog/index.html",context)

class BookListView(generic.ListView):
	#template=""
	model=Book
	templates="catalog/book_list"
	#queryset=Book.objects.all()[:5]
	context="Book_list"
	paginate_by=1
	def get_queryset(self):
		return Book.objects.all()[:4]


def OnLoan(request,id):
	book_inst = get_object_or_404(BookInstance, id=id)

	#print("***********************")
	if request.method == 'POST':
		book_inst.status="o"
		book_inst.borrower=request.user
		book_inst.save()

		return HttpResponse("Hi")

	return render(request,"catalog/index.html")


class BookDetailView(generic.DetailView):
	model=Book

class AuthorsListView(generic.ListView):
	model=Author
	context="author_list"
	paginate_by=1
	
class AuthorDetailView(generic.DetailView):
	model=Author
	'''
	def context_data(self,**kwargs):
		context=super(BookDetailView,self).get_context_data(**kwargs)
	context['some_data']="This is some data"
    '''

