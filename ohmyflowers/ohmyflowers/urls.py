"""ohmyflowers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from orderscrm.views import MainView, CompaniesView, OrdersView, CustomersView, CompanyDetailView, OrderDetailView, \
    CustomerDetailView, CompanyCreateView, OrderCreateView, CustomerCreateView, CompanyEditView, OrderEditView, \
    CustomerEditView, LoginView, logout_view, SearchView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('companies/', CompaniesView.as_view(), name='companies'),
    path('companies/create', CompanyCreateView.as_view(), name='company_create'),
    path('companies/<int:pk>', CompanyDetailView.as_view(), name='company'),
    path('companies/<int:pk>/edit', CompanyEditView.as_view(), name='company_edit'),
    path('orders/', OrdersView.as_view(), name='orders'),
    path('orders/create', OrderCreateView.as_view(), name='order_create'),
    path('orders/<int:pk>', OrderDetailView.as_view(), name='order'),
    path('orders/<int:pk>/edit', OrderEditView.as_view(), name='order_edit'),
    path('customers/', CustomersView.as_view(), name='customers'),
    path('customers/create', CustomerCreateView.as_view(), name='customer_create'),
    path('customers/<int:pk>', CustomerDetailView.as_view(), name='customer'),
    path('customers/<int:pk>/edit', CustomerEditView.as_view(), name='customer_edit'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('search/', SearchView.as_view(), name='search'),

]
