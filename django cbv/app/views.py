from django.shortcuts import render
#importing the different views
from django.views.generic import View,TemplateView,ListView,DetailView
from django.http import HttpResponse
#importing the model
from app import models









#class based view example
class CBYiew(View):
    def get(self,request):
        return HttpResponse("class based views are cool!")




# template based views
class IndexView(TemplateView):
    template_name = 'app/index.html'

    #def get_context_data(self, **kwargs):
        
       # context =  super().get_context_data(**kwargs)
        #context['injectme'] = 'basic injection'
       # return context




# list view example
class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.school




# detail view example
class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.school
    template_name = 'app/school_detail.html'


