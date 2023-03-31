"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpRequest
from django.shortcuts import render
from .models import Base, Command, Brigade, Battalion, Company
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_bases = Base.objects.all().count()
    num_battalions = Battalion.objects.all().count()

    context = {
        'num_bases': num_bases,
        'num_battalions': num_battalions,
    }

    # Render the HTML template index.html with the data in the context variable

    return render(request, 'index.html', context=context)

class BaseListView(generic.ListView):
    model = Base
    context_object_name = 'base_list'
    # queryset = Base.objects.filter(location='Fort Bragg')[:5]
    template_name = 'bases/template_list.html'
    paginate_by = 10

class BaseDetailView(generic.DetailView):
    model = Base

class BattalionListView(generic.ListView):
    model = Battalion
    context_object_name: 'battalion_list'
    template_name = 'battalions/detail_list.html'
    paginated_by = 10

class BattalionDetailView(generic.DetailView):
    model = Battalion


from app.models import UserProfile

class UserProfileUpdate(UpdateView):
    model = UserProfile
    fields = '__all__'
    success_url = reverse_lazy('index')