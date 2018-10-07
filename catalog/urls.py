from django.urls import path
from django.conf.urls import url
from . import views
										


urlpatterns=[

path('',views.index,name="index"),
path('books/',views.BookListView.as_view(),name="books"),
path('book/<int:pk>',views.BookDetailView.as_view(),name="book-detail"),
path('authors/',views.AuthorsListView.as_view(),name="authors"),
path('author/<int:pk>',views.AuthorDetailView.as_view(),name="author-detail"),
url(r'^onloan/(?P<id>.+)' ,views.OnLoan,name="onloan"),
path('mybooks/',views.LoanedBooksByUserListView.as_view(),name="my_borrowed"),


]								