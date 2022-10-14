from django import forms
from .models import Reservas, Huespedes

#
class ReservasFormCreate(forms.ModelForm):
  class Meta:
    model = Reservas
    #fields = '__all__'
    fields = ['id', 'fecha_reserva', 'nro_habitacion']
    widgets = {
      'fecha_reserva': forms.DateInput(attrs={'type': 'date'})     
    }
    
  def __init__(self, *args, **kwargs):
    # initialize form, which will create self.fields dict
    super(ReservasFormCreate, self).__init__(*args, **kwargs)
        
    self.fields['id'].widget.attrs.update({
      'class': 'mb-4',
    })

    self.fields['fecha_reserva'].widget.attrs.update({
      'class': 'mb-4',
    })
    
    self.fields['nro_habitacion'].widget.attrs.update({
      'class': 'mb-4',
    })
    
    
class HuespedesFormCreate(forms.ModelForm):
  class Meta:
    model = Huespedes
    fields = '__all__'
    widgets = {
      'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'})  
    }
    
  def __init__(self, *args, **kwargs):
    # initialize form, which will create self.fields dict
    super(HuespedesFormCreate, self).__init__(*args, **kwargs)
        
    self.fields['rut'].widget.attrs.update({
      'class': 'mb-4',
    })

    self.fields['nombre_completo'].widget.attrs.update({
      'class': 'mb-4',
    })
    
    self.fields['sexo'].widget.attrs.update({
      'class': 'mb-4',
    })
    
    self.fields['fecha_nacimiento'].widget.attrs.update({
      'class': 'mb-4',
    })