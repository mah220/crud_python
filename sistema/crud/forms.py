from django import forms
from.models import Veiculo
from.models import Motorista
from.models import Controle

###############
# FORM VEICULO
###############

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields ='__all__'

###############
# FORM MOTORISTA
###############

class MotoristaForm(forms.ModelForm):
    class Meta:
        model = Motorista
        fields ='__all__'

###############
# FORM CONTROLE E AJUSTES DE CAMPOS
###############

class ControleForm(forms.ModelForm):
    hora_saida = forms.TimeField(
        label='Hora Saida Ex: 12:00',
        widget=forms.TimeInput(
            format='%H:%M',
            attrs={
                'type': 'time'
            }
        ),
        input_formats=['%H:%M',
                          '%H:%M:%S',
        ],)
    data_saida = forms.DateField(
        label='Data Saida',
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'type': 'date'
            }
        ),
        input_formats=['%d/%m/%Y',
                       '%d-%m-%Y',
                       '%Y-%m-%d',      
                       '%m/%d/%Y',       
                       '%m/%d/%y'],    
    )
    data_retorno = forms.DateField(
        label='Data Retorno',
        widget=forms.DateInput(
            format='%d/%m/%Y',
            attrs={
                'type': 'date'
            }
        ),
        input_formats=['%d/%m/%Y',
                       '%d-%m-%Y',
                       '%Y-%m-%d',      
                       '%m/%d/%Y',      
                       '%m/%d/%y'],
    )
    class Meta:
        model = Controle
        fields ='__all__'