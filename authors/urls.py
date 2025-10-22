from django.urls import path

from . import views

app_name="authors"

urlpatterns = [
    path("list/", views.AuthorsList.as_view(), name="authors-list"),
    path("create/", views.AuthorsCreate.as_view(), name="authors-create"),
]