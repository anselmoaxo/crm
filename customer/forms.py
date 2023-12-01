from django import forms
from .models import Customer, Contato 


class DateInput(forms.DateInput):
    input_type = 'date'


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='SobreNome')
    email = forms.EmailField(label='E-Mail')
    bird_date = forms.DateField(label='Data Nacimento', widget=DateInput())
    area_cade = forms.CharField(label='DDD')
    phone_number = forms.CharField(label='Telefone')
    country = forms.CharField(label='Pais')
    state = forms.CharField(label='Estado')
    city = forms.CharField(label='Cidade')

    class Meta:
        model = Customer
        fields = (
            "first_name", 
            "last_name", 
            "email",
            "bird_date", 
            "area_cade", 
            "phone_number",
            "country",
            "state", 
            "city"
            )
        

class ContatoForm(forms.ModelForm):
    first_name = forms.CharField(label='Nome')
    last_name = forms.CharField(label='SobreNome')
    email = forms.EmailField(label='E-Mail')
    phone = forms.CharField(label='Telefone')
    cliente = forms.ModelChoiceField(queryset=Customer.objects.all(), label='Cliente')
    description = forms.CharField(label='Observação', widget=forms.Textarea)


    class Meta:
        model = Contato
        fields = (
            "first_name", 
            "last_name", 
            "email",
            "phone",
            "cliente",
            "description"
            )