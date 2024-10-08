from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_listing", views.add_listing, name="add_listing"),
    path("categories", views.get_categories, name="categories"),
    path("categorie/<str:name>", views.categorie, name="categorie"),
    path("<str:username>", views.profile, name="profile")

]
