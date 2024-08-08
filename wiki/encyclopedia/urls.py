from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki", views.index, name="index"),
    path("wiki/search", views.search, name="search"),
    path("wiki/add_entrie", views.add_entrie, name = "add_entrie"),
    path("wiki/edit/<str:title>", views.edit_entrie, name = "edit_entrie"),
    path("wiki/random", views.rendom_entrie, name="random" ),
    path("wiki/<str:title>", views.entry, name="entry")
    
]
