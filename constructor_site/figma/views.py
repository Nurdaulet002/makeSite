from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin, View
from .models import Good, Category
from.forms import CategoryForm, GoodForm


# FFFF
class ClientIndexView(TemplateResponseMixin,View):
    template_name = 'figma/client-site/index.html'

    def get (self, request, *args, **kwards):
        user_site = self.kwards.get('user_site', None)
        category = self.kwards.get('category', None)
        categories = Category.objects.all()
        goods = Good.objects.filter(top=True)
        if category:
            goods = goods.filter(category=category)
        return self.render_to_response({
            'categories': categories, 'goods': goods, 'user_site': user_site})


class ClientDetailView(TemplateResponseMixin,View):
    template_name = 'figma/client-site/detail_photo.html'
    
    def get (self, request, good=None, user_site=None):
        good = Good.objects.get(id=good)
        goods = Good.objects.all()
        return self.render_to_response({'good': good, 
            'user_site': user_site, 'goods': goods,})


class ConstructorIndexView(TemplateResponseMixin,View):
    template_name = 'figma/constructor-site/index.html'
    
    def get (self, request, user_site=None):
        categories = Category.objects.all()
        goods = Good.objects.filter(top=True)
        category_form = CategoryForm()
        good_form = GoodForm()
        return self.render_to_response({'user_site': user_site, 
            'category_form':category_form, 'good_form':good_form,
            'categories':categories, 'goods': goods})


class CategoryCreateview(View):

    def post (self, request, user_site=None):
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('figma:constructor', user_site=user_site)
        

class GoodCreateview(View):

    def post (self, request, user_site=None):
        good_form = GoodForm(request.POST, request.FILES)
        if good_form.is_valid():
            good_form.save()
            return redirect('figma:constructor', user_site=user_site)


class CategoryDeleteView(View):

    def post (self, request, user_site):
        category_id = request.POST.get('category_id')
        Category.objects.get(id=category_id).delete()
        return HttpResponse({'durys'})


class GoodDeleteView(View):
    
    def get (self, request, user_site): 
        good_id = request.GET.get('good_id')
        Good.objects.get(id=good_id).delete()
        return HttpResponse({'status': False, 'error': 'ADSD'})


class GoodUpdateView(View):
 
    def dispatch(self, request, good, user_site):
        self.good = Good.objects.get(id=good)
        return super().dispatch(request, good, user_site)

    def get (self, request, good, user_site):
        good_form = GoodForm(instance=self.good)
        return render(request, 'figma/constructor-site/update.html',{
            'good_form':good_form, 'good': self.good, 
            'user_site':user_site})  

    def post (self, request, good, user_site):
        good_form = GoodForm(request.POST,request.FILES, instance=self.good)
        if good_form.is_valid():
            good_form.save()
            return redirect('figma:constructor', user_site=user_site)



