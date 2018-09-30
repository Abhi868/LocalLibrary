from django.contrib import admin

from catalog.models import Author,BookInstance,Book,Genre
#admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display=["first_name","last_name","date_of_birth","date_of_death"]


admin.site.register(Author,AuthorAdmin)
#admin.site.register(BookInstance)
#admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display=['title','author','isbn']
#admin.register(Book, BookAdmin)

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
	list_filter=('status','due_back')

admin.site.register(Genre)

# Register your models here. 	
