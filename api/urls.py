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
    path('items/dificulty/<int:pk>/', views.ItemDificultySearch.as_view()),
    path('item/dificultys/', views.ItemDificultyAll.as_view()),
    path('items/', views.ItemsList.as_view()),
    path('search/item/<str:query>', views.SearchItem.as_view()),
    path('user/favorite/', views.UserFavoriteList.as_view()),
    path('user/favorite/add/<int:id>', views.UserFavoriteAdd.as_view()),
    path('user/favorite/clear/', views.UserFavoriteClear.as_view()),
    path('user/lastseen/', views.UserLastSeenList.as_view()),
    path('user/messages/', views.UserMessagesList.as_view()),
    path('user/message/add/', views.UserMessageAdd.as_view()),

    path('user/lastseen/update/<int:id>', views.UserLastSeenListUpdate.as_view()),
    path('user/info/', GetInfo.as_view()),
    path('user/update/', UpdateUser.as_view()),

]
