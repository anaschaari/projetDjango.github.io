from django.forms import inlineformset_factory
from django.shortcuts import render, redirect
from django.template import loader
from.models import Produit,Commande,Customer,Order
from.forms import FournisseurForm,ProduitForm,CreateUserForm,OrderForm,CustomerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from.filters import OrderFilter,CommandFilter
from .decorators import unauthenticated_user,allowed_users
from django.contrib.auth.models import Group
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect



def index1(request):
    list = Produit.objects.all()
    return render(request, 'vitrine2.html', {'list': list})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def fournisseurPage(request):
    if request.method == "POST":

        form=ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index1')
    else:

        form = ProduitForm()
    return render(request,'majProduits.html',{'form':form})
@login_required(login_url='login')
def index(request):
    listC=Commande.objects.all()
    myFilter=CommandFilter(request.GET, queryset=listC)
    listC=myFilter.qs
    context={'listC':listC,'myFilter':myFilter}
    return render(request,'commande.html',context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
	context={}
	return render(request, 'user.html', context)

def loginn(request):
    if request.user.is_authenticated:
        return redirect('index1')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('index1')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)
def logoutUser(request):
    logout(request)
    return redirect('login')
@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=user.username,
            )

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)
@login_required(login_url='login')
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'Commandform.html', context)
@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'settings2.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashbord(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending,'myFilter':myFilter}

    return render(request, 'dashboard.html', context)
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()
	context = {'customer':customer, 'orders':orders, 'order_count':order_count}
	return render(request, 'user.html',context)

def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	if request.method == 'POST':

		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'order_form.html', context)


def viewproduct(request,pk):
    products=Produit.objects.get(id=pk)
    context = {'products': products}
    return render(request,'productview.html',context)



