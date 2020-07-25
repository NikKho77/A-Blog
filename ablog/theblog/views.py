from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Post,History,Contacts,Prices,Hours

#def home(request):
 #   return render(request, 'home.html', {})

class HomeView(ListView):
    model = Post
    template_name  = 'home.html'

def index(request):
    return render(request, 'index.html', {})

class HistoryView(ListView):
    model = History
    template_name = 'history.html'

class ContactsView(ListView):
    model = Contacts
    template_name = 'contacts.html'

class PricesView(ListView):
    model = Prices
    template_name = 'prices.html'

class HoursView(ListView):
    model = Hours
    template_name = 'hours.html'

