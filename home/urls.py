from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('privacy_policy/', views.privacy_policy, name='privacy'),
    path('refund_policy/', views.refund_policy, name='refund'),
    path('terms_of_service/', views.terms_of_service, name='terms'),
    path('delivery_returns/', views.delivery_returns, name='delivery_returns'),
    path('how_to_shop/', views.how_to_shop, name='how_to_shop'),
    path('user_guide/', views.user_guide, name='user_guide'),
]
