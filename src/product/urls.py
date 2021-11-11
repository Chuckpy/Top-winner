from django.urls import path, include

from .views import ProductAPIView

app_name = 'product'

urlpatterns = [
    path('list/' , ProductAPIView.as_view(), name="list")
]