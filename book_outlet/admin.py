from django.contrib import admin
from .models import Book, Author, Adress, Country
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating")
    list_display = ("title", "author", "rating")


class AuthorAdmin(admin.ModelAdmin):
    list_filter = ("first_name", "last_name")
    list_display = ("first_name", "last_name")


class AdressAdmin(admin.ModelAdmin):
    list_filter = ("street", "postal_code", "city")
    list_display = ("street", "postal_code", "city")


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Adress, AdressAdmin)
admin.site.register(Country)
