from django.urls import path
from . import views

app_name = 'clothes'
urlpatterns = [
    path('',views.ClientIndexView.as_view(), name ='index'),
    path('good/list/<int:category>/',views.GoodListView.as_view(), name ='good_list'),
    path('good/list/<int:category>/<int:subcategory>',views.GoodListView.as_view(), name ='good_list'),
    path('detail/<int:good>',views.DetailView.as_view(), name ='detail'),
    path('add/bag/<int:good>',views.AddBagView.as_view(), name ='add_bag'),
    path('creat/category',views.CategoryCreatView.as_view(), name ='category_creat'),
] 