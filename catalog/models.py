import uuid
from django.db import models
from django.urls import reverse
# Create your models here.
class Genre(models.Model):
	name=models.CharField(max_length=80, help_text="Enter a book genre(e.g Science Fiction)")

	def __str__(self):
		return self.name

class Author(models.Model):
	first_name=models.CharField(max_length=20)
	date_of_birth=models.DateField(null=False,blank=False)
	date_of_death=models.DateField(null=True,blank=True)
	last_name=models.CharField(max_length=20)

	class Meta:
		ordering=['last_name','first_name']

	def get_absolute_url(self):
		return reverse('author-detail',args=[str(self.id)])

	def __str__(self):		
	 	return (self.first_name+" "+self.last_name)
	 	
class Book(models.Model):
	title=models.CharField(max_length=60)
	author=models.ForeignKey('Author', on_delete=models.CASCADE,help_text="Enter name of the author")
	summary=models.TextField(max_length=100,help_text="Enter description of the book")
	isbn=models.CharField('ISBN' ,max_length=13,help_text="13 character number <a href=https://www.isbn-international.org/content/what-isbn>what is ISBN number</a>")
	genre=models.ManyToManyField(Genre, help_text="Select Genre for this book ")

	def get_absolute_url(self):
		return reverse ("book-detail",args=[str(self.id)])


	def display_genre(self):
		return ','.join(genre.name for genre in self.genre.all()[:3])
	
	def __str__(self):
		return self.title
	display_genre.short_description='Genre'
		#return str(genre)

class BookInstance(models.Model):
	book=models.ForeignKey(Book, on_delete=models.CASCADE)
	id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="unique id for this book across whole library")
	imprint=models.CharField(max_length=200)
	loan_status=(('m',"maintenance"),('o',"On Loan"),('r',"reserved"),('a',"available"))
	due_back=models.DateField(null=True , blank=True)
	status=models.CharField(max_length=1,choices=loan_status,blank=False,help_text="Book availability",default="m")
 
	def __str__(self):
	   # return f'{self.id} ({self.book.title})'
	   return str(self.book.title) 

    #class Meta:
    #	ordering=['due_back']
 

