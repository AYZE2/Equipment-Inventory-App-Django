from django.shortcuts import render, redirect
from .models import Item , Product
from .forms import CreateItemForm, ItemForm , ProductForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm, UserUpdateForm,ProfileUpdateForm, CreateProductForm



# Create your views here.


@login_required
def home(request):
    item = Product.objects.all()
    context = {'item':item}
    return render(request, 'appone/home.html',context)



@login_required
def Blist(request, id ):
    listitem = Product.objects.get(id=id)

    if request.method == 'POST':
        form =ProductForm(request.POST, instance=listitem)
        if form.is_valid():
            listitem.save()
            return redirect('homepage')
    else:
            form= ProductForm(instance=listitem)    
    context ={'listitem':listitem,'form': form}
    return render(request, 'appone/Blist.html', context)
 
@login_required
def createItem(request):
    if request.method == "POST":
        form = CreateProductForm(request.POST)
        if form.is_valid():item = form.save()
        return redirect("homepage")
    else:
        form = CreateProductForm()
        return render(request, "appone/createitem.html", {"form": form})
    

def deleteItem(request,id):
     item=Item.objects.get(id=id)
     if request.method == "POST":
          item.delete()
          return redirect('homepage')
     return render(request, 'appone/deleteitem.html',{'item':item})

def register(request):
    if request.method =='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'account created for {username}!')
            return redirect('homepage')
    else:
        form = CreateUserForm()
    return render(request,'appone/register.html',{'form':form})


@login_required
def profile(request):
    context = {

    }
    return render(request, 'appone/profilepage.html', context)

def profile_update(request):
    if request.method=='POST':
        user_form= UserUpdateForm(request.POST, instance=request.user)
        profile_form=ProfileUpdateForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else:
        user_form=UserUpdateForm(instance=request.user)
        profile_form=ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form':profile_form,

    }
    return render(request, 'appone/profile_update.html', context)

