from django.contrib import admin
from .models import Company, Customer, Order


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'company_title', 'place_title', 'address')
    list_display_links = ('id', 'company_title')
    search_fields = ('company_title', 'place_title',)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'position')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'phone')


class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
