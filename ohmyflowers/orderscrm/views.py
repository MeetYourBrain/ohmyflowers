from django.utils.timezone import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, ListView, TemplateView
from .forms import CustomerCreationForm, CompanyCreationForm, OrderCreationForm, LoginForm
from .models import Company, Customer, Order
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.db.models import Q


def get_url(url):
    url = url[url.find('/') + 1:]
    url = url[:url.find('/')]
    return url


class MainView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        today = datetime.today()
        orders_today = Order.objects.filter(posted_at__year=today.year, posted_at__month=today.month,
                                           posted_at__day=today.day)
        return render(request, 'index.html', context={
            'orders': orders_today
        })


class CompaniesView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        companies = Company.objects.all()
        return render(request, 'companies.html', context={
            'companies': companies,
        })


class CompanyDetailView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, pk):
        company = get_object_or_404(Company, id=pk)
        title = f'Просмотр компании {company.company_title}'
        url = get_url(request.path)
        return render(request, 'detail_view_show.html', context={
            'company': company,
            'pk': pk,
            'title': title,
            'url': url
        })


class CustomersView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        customers = Customer.objects.all()
        companies = Company.objects.all()
        return render(request, 'customers.html', context={
            'customers': customers,
            'companies': companies,
        })


class CustomerDetailView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, pk):
        customer = get_object_or_404(Customer, id=pk)
        title = f'Заказчик {customer.name}'
        url = get_url(request.path)
        return render(request, 'detail_view_show.html', context={
            'customer': customer,
            'pk': pk,
            'title': title,
            'url': url,
        })


class OrdersView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        orders = Order.objects.all()
        return render(request, 'orders.html', context={
            'orders': orders,
        })


class OrderDetailView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        date_order = order.posted_at
        title = f'Запрос №{pk} от {date_order}'
        url = get_url(request.path)
        return render(request, 'detail_view_show.html', context={
            'order': order,
            'pk': pk,
            'title': title,
            'url': url,
        })


class CompanyCreateView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        form = CompanyCreationForm()
        return render(request, 'create.html', context={
            'form': form,
        })

    def post(self, request):
        company_create_form = CompanyCreationForm(request.POST)
        if company_create_form.is_valid():
            company_create_form.save()
            return redirect('companies')


class CustomerCreateView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        form = CustomerCreationForm()
        return render(request, 'create.html', context={
            'form': form,
        })

    def post(self, request):
        customer_create_form = CustomerCreationForm(request.POST)
        if customer_create_form.is_valid():
            customer_create_form.save()
            return redirect('customers')


class OrderCreateView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        form = OrderCreationForm()
        return render(request, 'create.html', context={
            'form': form,
        })

    def post(self, request):
        order_create_form = OrderCreationForm(request.POST)
        if order_create_form.is_valid():
            order_create_form.save()
            return redirect('orders')


class CompanyEditView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, pk):
        company = get_object_or_404(Company, id=pk)
        company_update_form = CompanyCreationForm(instance=company)
        url = get_url(request.path)
        return render(request, 'detail_edit.html', context={
            'form': company_update_form,
            'pk': pk,
            'url': url
        })

    def post(self, request, pk):
        company = get_object_or_404(Company, id=pk)
        company_update_form = CompanyCreationForm(request.POST, instance=company)
        if company_update_form.is_valid():
            company_update_form.save()
            return redirect('companies')


class CustomerEditView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, pk):
        customer = get_object_or_404(Customer, id=pk)
        customer_update_form = CustomerCreationForm(instance=customer)
        url = get_url(request.path)
        return render(request, 'detail_edit.html', context={
            'form': customer_update_form,
            'pk': pk,
            'url': url
        })

    def post(self, request, pk):
        customer = get_object_or_404(Customer, id=pk)
        customer_update_form = CustomerCreationForm(request.POST, instance=customer)
        if customer_update_form.is_valid():
            customer_update_form.save()
            return redirect('customers')


class OrderEditView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        order_update_form = OrderCreationForm(instance=order)
        url = get_url(request.path)
        return render(request, 'detail_edit.html', context={
            'form': order_update_form,
            'pk': pk,
            'url': url
        })

    def post(self, request, pk):
        order = get_object_or_404(Order, id=pk)
        order_update_form = OrderCreationForm(request.POST, instance=order)
        if order_update_form.is_valid():
            order_update_form.save()
            redirect('orders')

        return redirect('orders')


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', context={
            'form': form,
        })

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main')
        return render(request, 'login.html', context={
            'form': form,
        })


def logout_view(request):
    logout(request)
    return redirect('main')

class SearchView(LoginRequiredMixin, View):
    login_url = settings.LOGIN_URL

    def get(self, request):
        query = request.GET.get('q')
        customer_list = Customer.objects.filter(
            Q(name__icontains=query) | Q(phone__icontains=query)
        )
        company_list = Company.objects.filter(
            Q(company_title__icontains=query) | Q(place_title__icontains=query)
        )
        order_list = Order.objects.filter(
            Q(order_list__icontains=query) | Q(customer__name__icontains=query) | Q(company__company_title__icontains=query)
        )
        return render(request, 'search.html', context={
            'customers': customer_list,
            'companies': company_list,
            'orders': order_list,
        })
