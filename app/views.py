from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

from .models import Reservas, Huespedes
from .forms import ReservasFormCreate, HuespedesFormCreate 

# Create your views here.

#
def home(request):
  return render(request, 'app/home.html')


#
def bookingCreate(request):
  
  data = {
    'form1': ReservasFormCreate(),
    'form2': HuespedesFormCreate()
  } 
    
  if request.method == 'POST':
    form1 = ReservasFormCreate(data = request.POST)
    form2 = HuespedesFormCreate(data = request.POST)
    
    if form1.is_valid() and form2.is_valid():
      form1.save()
      form2.save()     
      
      return redirect('bookingCreateResponse')
      
    else:
      data["form1"] = form1
      data["form2"] = form2
  
  return render(request, 'app/bookingCreate.html', data)


#
def bookingResponse(request):      
  identificador = request.POST['id']
  fechaReserva = request.POST['fecha_reserva']
  nHabitacion = request.POST['nro_habitacion']
  
  # args = {
  #   'id': identificador,
  #   'fecha_reserva': fechaReserva    
  # }
  
  reservation = Reservas.objects.create(id=identificador, fecha_reserva=fechaReserva, nro_habitacion=nHabitacion)  
  
  return render(request, 'app/bookingCreateResponse.html', {'r': reservation})

#
def bookingUpdate(request):
  return render(request, 'app/bookingUpdate.html')

#
def bookingDelete(request):
  return render(request, 'app/bookingDelete.html')

#
def bookingSearch(request):
  return render(request, 'app/bookingSearch.html')

#
def bookingTable(request):
  reservas = Reservas.objects.all()
  
  data = {
    "reservas": reservas
  }
  
  return render(request, 'app/bookingTable.html', data)
