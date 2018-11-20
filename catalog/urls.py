from django.urls import path,include
from django.conf.urls import url
from catalog import views

										


urlpatterns=[


url(r'^signup/',views.signUp,name="signup"),
path('',views.index,name="index"),
path('books/',views.BookListView.as_view(),name="books"),
path('book/<int:pk>',views.BookDetailView.as_view(),name="book-detail"),
path('authors/',views.AuthorsListView.as_view(),name="authors"),
path('author/<int:pk>',views.AuthorDetailView.as_view(),name="author-detail"),
url(r'^onloan/(?P<id>.+)' ,views.OnLoan,name="onloan"),
path('mybooks/',views.LoanedBooksByUserListView.as_view(),name="my_borrowed"),

url(r'^allbooks/',views.BorrowedBooksLibrarianListView.as_view(),name="borrowed_books"),
url(r'^renew/(?P<pk>.+)',views.ChangeDueBackDetailView.as_view(),name="change_dueback"),
url(r'^change_duedate/(?P<id>.+)',views.ChangeDueBack,name="duedate_changed"),

path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),

path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),



]	
						