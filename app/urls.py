from django.urls import path
from .views import home, bookingCreate, bookingTable, bookingSearch, bookingUpdate, bookingDelete, bookingResponse

urlpatterns = [
  path('', home, name='home'),
  path('bookingCreate/', bookingCreate, name='bookingCreate'),
  path('bookingCreateResponse/', bookingResponse, name='bookingCreateResponse'),
  path('bookingTable', bookingTable, name='bookingTable'),
  path('bookingSearch/', bookingSearch, name='bookingSearch'),
  path('bookingUpdate/', bookingUpdate, name='bookingUpdate'),
  path('bookingDelete/', bookingDelete, name='bookingDelete'),
]