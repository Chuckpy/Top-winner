from django.db import models
from django.contrib.auth.models import User


class Customer(User):

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    image = models.ImageField(null=True, blank=True, upload_to="uploads/user/img/")
    phone_number = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    date_of_birth = models.CharField(max_length=30, blank=True, null=True, default=None)

    USERNAME_FIELD = 'email'
    REQUIREMENTS_FIELD = ['username','password']

    def __str__(self):   
        return self.first_name