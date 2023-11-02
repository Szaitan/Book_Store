from django.urls import path
from . import views

urlpatterns = [
    path("<slug:slug>", views.detail_book_page, name="detail_book_page"),
    path("", views.index_page, name="index_page"),
]
