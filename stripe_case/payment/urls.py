from django.urls import path

from payment import views


urlpatterns = [
    path('<slug:price_id>/buy/', views.buy),
    path('<int:item_id>/item/', views.item_detail, name='item_detail'),
    path('<int:order_id>/order/', views.order_detail, name='item_detail'),
]
