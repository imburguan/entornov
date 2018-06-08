from  django import forms
#from models import Pessoas
from .models import Faixas
#from .forms import UserCreativeForm

# Importa modelo


# A = 1
# B = 2
# C = 4
# D = 4
# E = 5
# F = 6
#
# PREFERRED_EDADE_CHOICES = (
#     (A, '20 anos ou menos'),
#     (B, '21 - 30 anos'),
#     (C, '31 - 40 anos'),
#     (D, '41 - 50 anos'),
#     (E, '51 - 60 anos'),
#     (F, '61 anos ou mais'),
# )
#
# class EdadesForm(form.Form):
#     print ("########## Iliana la mas inteligente del mundo que va a Stanford ########## ")
#     #nome = forms.CharField(widget=forms.TextInput(attrs={'onmouseover':'meuMouseOver()', 'onmouseout':'meuMouseOut()'}))
#     preferred_edad = form.ChoiceField(choices=PREFERRED_EDADE_CHOICES,
#                                         widget=forms.RadioSelect())


# Cria classe do form para o modelo
# class PessoasForm(forms.ModelForm):
#     nome = forms.CharField(widget=forms.TextInput(attrs={'onmouseover':'meuMouseOver()', 'onmouseout':'meuMouseOut()'}))
#
#     # Associa formulario ao modelo
#     class Meta:
#         model = Pessoas


#class FaixasForm(forms.Form):
#class FaixasForm(forms.ModelForm):
class FaixasForm(forms.Form):
        #############
    class Meta:
        model = Faixas
        #fields = (faixa_text')
        #############
    #faixa_text = forms.CharField(widget=forms.TextInput(attrs={'onmouseover':'meuMouseOver()', 'onmouseout':'meuMouseOut()'}))
        faixa_text = forms.CharField(max_length=60)
        print ("ESta es una prueba"), faixa_text
