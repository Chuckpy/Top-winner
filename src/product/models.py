from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)



class Product(models.Model): 
    # category = models.ManyToManyField(Category, related_name="products", blank=True)   
    name = models.CharField('Nome',max_length=100)
    slug = AutoSlugField(unique=True, always_update=False, populate_from="name", null=True)
    description = models.TextField('Descrição',max_length=500, blank=True)
    reference_code = models.IntegerField('Código de Referência')
    internal_code=models.IntegerField('Código Interno', null=True)
    price = models.DecimalField('Preço',max_digits=10, decimal_places=2)
    image = models.ImageField('Imagem', upload_to="products/%Y/%m/%d", blank=True)
    # TODO weight = models.DecimalField('Peso', default=0, blank=True, max_digits=10, decimal_places=3)
    is_available = models.BooleanField('Disponivel', default=True)

    # available = AvailableManager()
    
    def __str__(self):
        return f'{self.name}-{self.pk}'
    
    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"slug": self.slug})
            
    class Meta :
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"