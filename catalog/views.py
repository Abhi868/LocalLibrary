
from datetime import date
from .forms import BookRenewForm
from django.shortcuts import render

from django.shortcuts import render,HttpResponse,get_object_or_404,reverse

from django.views import generic
from catalog import forms
from . models import Book,BookInstance, Author, Genre
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
from django.core.cache import cache
from django.contrib.auth.decorators import login_required
import redis
from django.conf import settings
import pickle
# from catalog import/
r=redis.StrictRedis(host=settings.REDIS_HOST, port = settings.REDIS_PORT, db =settings.REDIS_DB, decode_responses = True)

from catalog.forms import SignUpForm

def signUp(request):
	if request.method=='POST':
		
		
		form=SignUpForm(request.POST)
		if form.is_valid():
			user=form.save()
			user.refresh_from_db()
			user.profile.email_id=form.cleaned_data.get('email_id')
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user.save()
			user=authenticate(username=user.username,password=raw_password)
			login(request,user)
			return redirect('home')
	else:
		form=SignUpForm()
	return render(request,'catalog/signup.html',{'form':form})
            # # user = authenticate (username=user.username, password=raw_password)
            # login(request, user)
            # return redirect('home')
    # else:
    # #     form = SignUpForm()
    # return render(request, 'signup.html', {'form': form})


# Create your views here.

@login_required
def home(request):
	return render(request,"catalog/home.html")

class AuthorCreate(CreateView):
	model=Author
	template_name="catalog/author_create_form.html"
	#print("hi")
	fields="__all__"
	success_url=reverse_lazy('authors')


class AuthorDelete(DeleteView):
	model=Author
	success_url=reverse_lazy('authors')

class AuthorUpdate(UpdateView):
	model=Author
	
	fields="__all__"
	temolate_name_suffix="catalog/author_update_form.html"
	success_url=reverse_lazy('authors')


class BorrowedBooksLibrarianListView(LoginRequiredMixin,generic.ListView):
	model="BookInstance"
	template_name="catalog/librarian_borrowed_books_list.html"

	def get_queryset(self):
		return BookInstance.objects.order_by('due_back')


class ChangeDueBackDetailView(PermissionRequiredMixin,generic.DetailView):
	
	model="BookInstance"
	permission_required="catalog.can_mark_returned"
	
	
	context_object_name="bookinstance_list"
	queryset=BookInstance.objects.all()
	
	template_name="catalog/change_due_back_detail.html"
	
	#def get_queryset(self):
	#	return BookInstance.objects.all()

class ChangeDueDateDetailView(generic.DetailView):

	model = BookInstance


def ChangeDueBack(request, id):
	print(request.POST['duedate'])
	book_inst = get_object_or_404(BookInstance, id=id)
	book_inst.due_back = request.POST['duedate']

	book_inst.save()
	new_book_detail=get_object_or_404(BookInstance,id=id)
	context={"book" : new_book_detail}
	return render(request,"catalog/after_due_date_changed.html",context)



class LoanedBooksByUserListView(LoginRequiredMixin,generic.ListView):
	model="BookInstance"
	template_name="catalog/bookinstance_list_borrowed_user.html"
	paginate_by=2
	#context="booklist"
	
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
	paginate_by=2
	def get_queryset(self):
		return Book.objects.all()
		# if r.get('book3'):
		# 	book =pickle.loads(r.get('book3'))
		# 	print('foun book object in cache')
		# # if r.has_key('book'):
		# # # if 'book' in cache:
		# # 	print('Inside cache')
		# # 	book=r.get('book')
		# 	# return  book
		# else:
		# 	print('set value inside cache')
		# 	book=Book.objects.all()
		# 	# book=list(Book.objects.values_list('id','isbn' ,'author_id' ,'summary'))
		# 	# r.setex('book',60*3,book)
		# 	r.set('book3' ,  pickle.dumps(book))
		# 	# print('book object' , json.loads(r.hgetall('book3')['student']))
		# print('book' , book )
		# return book

def renew_book_librarian(request,id):

	book_instance=get_object_or_404('BookInstance',id=id)
	if request.method=="POST":
		form_instance=BookRenewForm(request.POST)
		if form_instance.is_valid:
			book_instance.due_back=form_instance.cleaned_data['renewal_date']
			book_instance.save()
			return HttpResponseRedirect(reverse('my_borrowed'))

		else:
			proposed_date=datetime.date.today+datetime.date.timedelta(weeks=3)
			form_instance=BookrenewForm(initial={'proposed_date':proposed_date})

		context={'form':form_instance,

				'book_instance'	:book_instance,	}
		return render(request,"catalog/book_renew_librarian.html",context)



		


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
	# paginate_by=1
	
class AuthorDetailView(generic.DetailView):
	model=Author
	'''
	def context_data(self,**kwargs):
		context=super(BookDetailView,self).get_context_data(**kwargs)
	context['some_data']="This is some data"
    '''

