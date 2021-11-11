from django.contrib import admin


from .models import Product

class ProductAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados do produto :', {
            'fields':('image','name', 'description', 'reference_code')
        } ),
        ('Dados de preço :', {
          'fields':('price', 'is_available')  
        } )
    )
    list_filter= ('id', 'price')
    list_display = ('name','description','price' ) 
    search_fields = ('id', 'name', 'reference_code', 'internal_code')
    
    
admin.site.register(Product, ProductAdmin)