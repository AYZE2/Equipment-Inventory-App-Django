from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Item ,Profile, Product

class CreateUserForm(UserCreationForm):
    email= forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']



class CreateItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = '__all__'

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class CreateProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'address']

