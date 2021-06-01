from django.urls import path,include
from django.conf.urls import url
from .import views


urlpatterns=[
    path('',views.index1),
    path('commandes/',views.index,name="index"),
    path('login/',views.loginn,name="login"),
    path('register/',views.register,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('fournisseur/',views.fournisseurPage,name="fournisseurPage"),
    path('account/', views.accountSettings, name="account"),
    path('dashboard/',views.dashbord,name="dashboard"),
    path('customer/',views.customer,name="customer"),
    path('view/<int:pk>/', views.viewproduct, name="view"),


]