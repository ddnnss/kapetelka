from django.urls import path,include
from . import views
from user.views import *

urlpatterns = [
    path('static/copyright/', views.CopyrightText.as_view()),
    path('static/terms/', views.TermsText.as_view()),
    path('categories/', views.Categories.as_view()),
    path('tags/', views.Tags.as_view()),
    path('categories/tag/<int:id>/', views.CategoriesByTag.as_view()),
    path('item/<int:pk>/', views.ItemDetail.as_view()),
    path('user/favorite/<int:pk>/', views.UserFavoriteList.as_view()),
    path('user/info/', GetInfo.as_view()),
    path('user/update/', UpdateUser.as_view()),

]
