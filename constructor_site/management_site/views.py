from django.shortcuts import render, redirect
from django.views.generic.base import TemplateResponseMixin, View
from django.views.generic.list import ListView
from .forms import DemandForm
from .models import Site, UserSite, Category


class InformationView(TemplateResponseMixin, View):
    template_name = 'management/information.html'

    def get(self,request):
        demand_form = DemandForm()
        return self.render_to_response({'demand_form': demand_form})

    def post(self, request):
        demand_form = DemandForm(request.POST)
        if demand_form.is_valid():
            demand_form.save()
            return redirect('management:information_page')
        return self.render_to_response({'demand_form': demand_form})



class MySiteListView(ListView):
    template_name = 'management/mysite.html'
    model = UserSite
	

class SiteListView(ListView):
    template_name = 'management/site_list.html'
    model = Site
    context_object_name = 'sites'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        context['categories'] = categories
        return context


