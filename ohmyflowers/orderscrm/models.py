from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Customer(models.Model):
    name = models.CharField(max_length=64, verbose_name='ФИО')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон')
    position = models.CharField(max_length=30, verbose_name='Должность')
    company = models.ManyToManyField('Company', related_name='companies', verbose_name='Компания')

    def __str__(self):
        return f'{self.name} {self.phone}'

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Company(models.Model):
    company_title = models.CharField(max_length=64, verbose_name='Название компании')
    place_title = models.CharField(max_length=64, verbose_name='Название заведения')
    address = models.CharField(max_length=256, verbose_name='Фактический адрес')
    payment_details = models.CharField(max_length=512, verbose_name='ИНН')

    def __str__(self):
        return f'{self.company_title}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', verbose_name='Заказчик', null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='orders', verbose_name='Компания')
    order_list = models.TextField(max_length=2048, verbose_name='Тело заказа')
    order_sum = models.IntegerField(verbose_name='Сумма заказа', default=0)
    offer = models.BooleanField(verbose_name='КП', default=False)
    offer_date = models.DateField(verbose_name='КП выставлен', blank=True, null=True, auto_now=False, auto_now_add=False)
    payment = models.BooleanField(verbose_name='Счет выставлен', default=False)
    payment_date = models.DateField(verbose_name='Дата счета', blank=True, null=True)
    payment_done = models.BooleanField(verbose_name='Счет оплачен', default=False)
    payment_done_date = models.DateField(verbose_name='Дата оплаты', blank=True, null=True)
    payment_sum = models.IntegerField(verbose_name='Сумма оплаты', default=0)
    order_completed = models.BooleanField(verbose_name='Заказ выполнен', default=False)
    order_completed_date = models.DateField(verbose_name='Дата выполнения', blank=True, null=True)
    order_done = models.BooleanField(verbose_name='Заказ сдан', default=False)
    order_done_date = models.DateField(verbose_name='Дата сдачи', blank=True, null=True)
    posted_at = models.DateField(auto_now_add=True, verbose_name='Дата размещения')
    canceled = models.BooleanField(verbose_name='Заказ отменен', default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='order_created',
                                 verbose_name='Создатель запроса')

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self._offer = self.offer
        self._payment = self.payment
        self._payment_done = self.payment_done
        self._order_completed = self.order_completed
        self._order_done = self.order_done

    def save(self, *args, **kwargs):
        if self._offer != self.offer:
            self.offer_date = datetime.now()
        if self._payment != self.payment:
            self.payment_date = datetime.now()
        if self._payment_done != self.payment_done:
            self.payment_done_date = datetime.now()
        if self._order_completed != self.order_completed:
            self.order_completed_date = datetime.now()
        if self._order_done != self.order_done:
            self.order_done_date = datetime.now()
        super(Order, self).save(*args, **kwargs)

    def __str__(self):
        return f'Заказ №{self.pk} от {self.posted_at} '

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
