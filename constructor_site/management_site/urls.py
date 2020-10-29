from django.urls import path
from . import views
app_name = 'management'

urlpatterns = [
    path('',views.InformationView.as_view(), name = 'information_page'),
    path('mysite',views.MySiteListView.as_view(), name = 'mysite_page'),
    path('site/list',views.SiteListView.as_view(), name = 'site_list_page'),

]