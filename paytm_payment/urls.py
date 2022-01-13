from django.urls import path
from django.contrib.auth.views import LoginView
from .views import initiate_payment, callback

urlpatterns = [
        path('', LoginView.as_view(template_name='login.html'), name='login'),
        path('pay/', initiate_payment, name='pay'),
        path('callback/', callback, name='callback'),
    ]