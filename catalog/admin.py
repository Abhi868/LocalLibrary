from django.contrib import admin

from catalog.models import Author,BookInstance,Book,Genre
#admin.site.register(Author)

class AuthorInline(admin.TabularInline):
	model=Author	
class AuthorAdmin(admin.ModelAdmin):
	fieldset=["first_name",("date_of_birth","date_of_death")]
	list_display=["first_name","last_name","date_of_birth","date_of_death"]
#	inlines=[AuthorInline]
admin.site.register(Author,AuthorAdmin)
#admin.site.register(BookInstance)
#admin.site.register(Book)




class BookInstanceInline(admin.TabularInline):
	model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display=['title','author','isbn']
	inlines=[BookInstanceInline]


#admin.register(Book, BookAdmin)

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
	list_display=('book','status','borrower','due_back','id')
	list_filter=('status','due_back')

	#fieldset=(('Book_Info',{'fields':('book','id','imprint')}),
	#	('Availability',{'fields':('status','due_back')}))

	fieldsets = ((None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

admin.site.register(Genre)

# Register your models here. 	




