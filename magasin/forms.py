
from django.forms import ModelForm
from .models import Produit,Commande,Customer,Order
from django import  forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProduitForm(ModelForm):
    class Meta :
        model = Produit
        fields = "__all__"
        #pour tous les champs de la table
class OrderForm(ModelForm):
    class Meta:
        model= Order
        fields = "__all__"
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FournisseurForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField(label='E-Mail')

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

