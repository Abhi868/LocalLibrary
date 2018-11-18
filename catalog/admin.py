from django.contrib import admin

from catalog.models import Author,BookInstance,Book,Genre
#admin.site.register(Author)

class BookInline(admin.TabularInline):
	model=Book	

class AuthorAdmin(admin.ModelAdmin):
	fieldset=["first_name",("date_of_birth","date_of_death")]
	list_display=["first_name","last_name","date_of_birth","date_of_death"]
	inlines=[BookInline]
admin.site.register(Author,AuthorAdmin)





class BookInstanceInline(admin.TabularInline):
	model=BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display=['title','author','isbn']
	inlines=[BookInstanceInline]


#admin.register(Book, BookAdmin)

@admin.register(BookInstance)
class BookInstance(admin.ModelAdmin):
	list_display=('pk','book','status','borrower','due_back','id','imprint')
	list_filter=('status','due_back')

	#fieldset=(('Book_Info',{'fields':('book','id','imprint')}),
	#	('Availability',{'fields':('status','due_back')}))

	fieldsets = (('Book_Info', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )

admin.site.register(Genre)

# Register your models here. 	




