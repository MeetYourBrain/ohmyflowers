from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=64, verbose_name='ФИО')
    phone = models.CharField(max_length=20, unique=True, verbose_name='Телефон')
    position = models.CharField(max_length=30, verbose_name='Должность')
    company = models.ManyToManyField('Company', related_name='companies', verbose_name='Компания')

    def __str__(self):
        return f'Заказчик {self.name}'

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


class Company(models.Model):
    company_title = models.CharField(max_length=64, verbose_name='Название компании')
    place_title = models.CharField(max_length=64, verbose_name='Название заведения')
    address = models.CharField(max_length=256, verbose_name='Фактический адрес')
    payment_details = models.TextField(max_length=512, verbose_name='Реквизиты оплаты')

    def __str__(self):
        return f'Компания {self.company_title}'

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders', verbose_name='Заказчик')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='orders', verbose_name='Компания')
    order_list = models.TextField(max_length=2048, verbose_name='Тело заказа')
    order_sum = models.IntegerField(verbose_name='Сумма заказа', default=0)
    offer = models.BooleanField(verbose_name='Коммерческое предложение')
    payment = models.BooleanField(verbose_name='Счет выставлен')
    payment_done = models.BooleanField(verbose_name='Счет оплачен')
    payment_sum = models.IntegerField(verbose_name='Сумма оплаты', default=0)
    order_completed = models.BooleanField(verbose_name='Заказ выполнен')
    order_done = models.BooleanField(verbose_name='Заказ сдан')
    posted_at = models.DateField(auto_now_add=True, verbose_name='Дата размещения')

    def __str__(self):
        return f'Заказ №{self.pk} от {self.posted_at} '

    class Meta:
        verbose_name = 'Запрос'
        verbose_name_plural = 'Запросы'
