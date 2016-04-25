from django.contrib import admin
from books.models import Publisher, Author, Book


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')  # displays email on admin
    search_fields = ('first_name', 'last_name')  # search bar


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publication_date',)  # filter
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    # fields = ('title', 'authors', 'publisher')   - publication_date non editable
    filter_horizontal = ('authors',)  # multiselection splitted on ManyToManyField
    raw_id_fields = ('publisher',)  # magnifier and changes select to input


admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
