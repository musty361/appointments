from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('book/', views.create_appointment, name='book_appointment'),
    path('book', views.create_appointment, name='book_appointment_no_slash'),  # Without trailing slash
    path('checkout/<int:appointment_id>/', views.checkout, name='checkout'),
    path('process-payment/<int:appointment_id>/', views.process_payment, name='process_payment'),
    path('payment-success/<int:appointment_id>/', views.payment_success, name='payment_success'),
    path('appointments/', views.appointment_list, name='appointment_list'),
]
