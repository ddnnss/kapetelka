from django.urls import path,include
from . import views
from user.views import *

urlpatterns = [
    path('suppliers/', views.Suppliers.as_view()),
    path('supplier/create/', views.SupplierCreate.as_view()),
    path('supplier/delete/<int:pk>', views.SupplierDelete.as_view()),
    path('supplier/edit/<int:pk>', views.SupplierEdit.as_view()),

    path('testers/', views.Testers.as_view()),
    path('tester/create/', views.TesterCreate.as_view()),
    path('tester/delete/<int:pk>', views.TesterDelete.as_view()),
    path('tester/edit/<int:pk>', views.TesterEdit.as_view()),

    path('categories/', views.Categories.as_view()),
    path('category/create/', views.CategoryCreate.as_view()),
    path('category/delete/<int:pk>', views.CategoryDelete.as_view()),
    path('category/edit/<int:pk>', views.CategoryEdit.as_view()),

    path('items/', views.Items.as_view()),
    path('item/create/', views.ItemCreate.as_view()),
    path('item/get_image/', views.ItemGetImage.as_view()),
    path('item/edit/<int:pk>', views.ItemUpdate.as_view()),


    path('sorts/', views.Sorts.as_view()),
    path('sort/delete/<int:pk>', views.SortDelete.as_view()),

    path('equips/', views.Equips.as_view()),
    path('equip_tests/', views.EquipTests.as_view()),
    path('equip_test/create/', views.EquipTestsCreate.as_view()),

    path('user/me/', GetUser.as_view()),
    path('user/update/', UpdateUser.as_view()),

]
