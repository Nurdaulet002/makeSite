from django.urls import path
from . import views

app_name = 'figma'
urlpatterns = [
    path('',views.ClientIndexView.as_view(), name ='index'),
    path('<int:category>',views.ClientIndexView.as_view(), name ='index'),
    path('detail/<int:good>',views.ClientDetailView.as_view(), name ='detail'),
    path('Constructor/',views.ConstructorIndexView.as_view(), name = 'constructor'),
    path('Category/create/',views.CategoryCreateview.as_view(), name = 'createcategory'),
    path('Good/create',views.GoodCreateview.as_view(), name = 'creategood'),
    path('category/delete',views.CategoryDeleteView.as_view(), name ='category_delete'),
    path('updategood<int:good>',views.GoodUpdateView.as_view(), name ='update_good'),
    path('good/delete',views.GoodDeleteView.as_view(), name ='good_delete'),
    
] 
