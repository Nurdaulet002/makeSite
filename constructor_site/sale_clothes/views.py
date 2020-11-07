from django.shortcuts import render,redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib import messages
from .forms import DemandForm
from .models import Good, Category, UnderCategory, AdditionalData, Comment
from mini_crm.models import Order
from .forms import CommentForm
import datetime


class ClientIndexView(TemplateResponseMixin,View):
    template_name = 'clothes/client-site/information.html'

    def dispatch(self, *args, **kwards):
        self.user_site = self.kwards.get('user_site')
        self.categories = Category.objects.all(
            user_site__url_address=self.user_site)
        self.goods = Good.objects.filter(
            is_top=True, user_site__url_address=self.user_site)
        return super().dispatch(*args, **kwards)

    def get (self, request, *args, **kwards):
        demand_form = DemandForm()
        return self.render_to_response({
            'categories': self.categories,
            'goods': self.goods, 'demand_form': demand_form})

    def post(self, request):
        demand_form = DemandForm(request.POST)
        if demand_form.is_valid():
            demand_form.save()
            messages.add_message(request, messages.SUCCESS, 'Ваша заявка отправлена успешна')
            return redirect('clothes:index', user_site=self.user_site)
        return self.render_to_response({
            'categories': self.categories,
            'goods': self.goods, 'demand_form': demand_form})


class GoodListView(TemplateResponseMixin,View):
    template_name = 'clothes/client-site/good_list.html'

    def get (self, request, category=None, subcategory=None):
        undercategories = None
        list_goods = Good.objects.filter(is_top=True)
        categories = Category.objects.all()
        if category:
            goods = Good.objects.filter(is_top=True)
            undercategories = UnderCategory.objects.filter(category=category)
        if subcategory:
            goods = Good.objects.filter(undercategory=subcategory)
        return self.render_to_response({
            'categories': categories, 'undercategories': undercategories,
            'goods': goods, 'category': category, 'list_goods': list_goods})


class DetailView(TemplateResponseMixin,View):
    template_name = 'clothes/client-site/detail.html'

    def get(self, request, good):
        categories = Category.objects.all()
        good = Good.objects.get(id=good)
        goods = Good.objects.filter(is_top=True)
        coment_form = CommentForm()
        coments = Comment.objects.filter()
        date = datetime.datetime.now()
        return self.render_to_response({'good': good, 'goods': goods,
            'coment_form': coment_form, 'coments':coments, 'date':date, 'categories': categories})

    def post(self, request, good):
        coment_form = CommentForm(request.POST)
        if coment_form.is_valid():
           coment_form.save()
           return redirect('clothes:detail', good=good)
        return self.render_to_response({'coment_form': coment_form})
        

class AddBagView(View):
    def get(self, request, good):
        good_obj = Good.objects.get(id=good)
        order = Order.objects.create(base_object=good_obj)
        return redirect('clothes:detail', good=good)


class CategoryCreatView(TemplateResponseMixin,View):
    template_name = 'clothes/constructor-site/information.html'

    def get(self, request, user_site, category=None):
        categories = Category.objects.filter(user_site__url_address=user_site)
        return self.render_to_response({'categories': categories})
