from .models import Customer

from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def count_widgets():
    return Customer.objects.count()


@shared_task
def rename_widget(widget_id, first_name):
    w = Customer.objects.get(id=widget_id)
    w.first_name = first_name
    w.save()