from django.urls import path
from . import views
from .views import HomeView,HistoryView,ContactsView,PricesView,HoursView

urlpatterns = [
  #  path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('', views.index, name="index"),
    path('history.html/', HistoryView.as_view(), name="history"),
    path('contacts.html/', ContactsView.as_view(), name="contacts"),
    path('prices.html/', PricesView.as_view(), name="prices"),
    path('hours.html/' , HoursView.as_view(), name="hours"),


]