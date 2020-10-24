from django.urls import path,include
from . import views
from user.views import *

urlpatterns = [
    path('manufacturers/', views.Manufacturers.as_view()),
    path('manufacturer/create/', views.ManufacturerCreate.as_view()),
    path('manufacturer/delete/<int:pk>', views.ManufacturerDelete.as_view()),
    path('manufacturer/edit/<int:pk>', views.ManufacturerEdit.as_view()),

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

    path('subcategories/', views.SubCategories.as_view()),
    path('subcategory/create/', views.SubCategoryCreate.as_view()),
    path('subcategory/delete/<int:pk>', views.SubCategoryDelete.as_view()),
    path('subcategory/edit/<int:pk>', views.SubCategoryEdit.as_view()),

    path('items/', views.Items.as_view()),
    path('item/create/', views.ItemCreate.as_view()),
    path('item/get_image/', views.ItemGetImage.as_view()),
    path('item/edit/<int:pk>', views.ItemUpdate.as_view()),

    path('sorts/', views.Sorts.as_view()),
    path('sort/delete/<int:pk>', views.SortDelete.as_view()),

    path('equips/', views.Equips.as_view()),
    path('equip_date_type/', views.EquipTests.as_view()),

    path('equip_tests/', views.EquipTests.as_view()),
    path('equip_test/create/', views.EquipTestsCreate.as_view()),

    path('equip_test_date_types/', views.EquipTestDateTypes.as_view()),
    path('equip_test_date_type/create/', views.EquipTestDateTypeCreate.as_view()),
    path('equip_test_date_type/delete/<int:pk>', views.EquipTestDateTypeDelete.as_view()),
    path('equip_test_date_type/edit/<int:pk>', views.EquipTestDateTypeEdit.as_view()),

    path('equip/create/', views.EquipCreate.as_view()),
    path('equip/delete/<int:pk>', views.EquipDelete.as_view()),
    path('equip/edit/<int:pk>', views.EquipEdit.as_view()),

    path('sample_types/', views.SampleTypes.as_view()),
    path('sample_type/create/', views.SampleTypeCreate.as_view()),
    path('sample_type/delete/<int:pk>', views.SampleTypeDelete.as_view()),
    path('sample_type/edit/<int:pk>', views.SampleTypeEdit.as_view()),

    path('sample_states/', views.SampleStates.as_view()),
    path('sample_state/create/', views.SampleStateCreate.as_view()),
    path('sample_state/delete/<int:pk>', views.SampleStateDelete.as_view()),
    path('sample_state/edit/<int:pk>', views.SampleStateEdit.as_view()),

    path('samples/', views.Samples.as_view()),
    path('sample/create/', views.SampleCreate.as_view()),
    path('sample/delete/<int:pk>', views.SampleDelete.as_view()),
    path('sample/edit/<int:pk>', views.SampleEdit.as_view()),
    path('sample/close/<int:pk>', views.SampleEdit.as_view()),
    path('sample/get_image/', views.SampleGetImage.as_view()),

    path('sample_expiriments/', views.SampleExpiriments.as_view()),
    path('sample_expiriment/create/', views.SampleExpirimentCreate.as_view()),
    path('sample_expiriment/delete/<int:pk>', views.SampleExpirimentDelete.as_view()),
    path('sample_expiriment/edit/<int:pk>', views.SampleExpirimentEdit.as_view()),



    path('sample_expiriment_field/delete/<int:pk>', views.SupplierDelete.as_view()),
    path('sample_expiriment_field/edit/<int:pk>', views.SupplierEdit.as_view()),





    path('user/me/', GetUser.as_view()),
    path('user/update/', UpdateUser.as_view()),

]
