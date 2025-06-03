from django.contrib import admin
from django.urls import path
from My_Car_rental import views
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .api_views import CarViewSet, BookingViewSet, FeedbackViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.car_list, name='car_list'),  # Home page shows car list
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', views.index, name='index'),
]

router = DefaultRouter()
router.register('api/cars', CarViewSet)
router.register('api/bookings', BookingViewSet)
router.register('api/feedbacks', FeedbackViewSet)

urlpatterns = [
    path('payment/create_session/<int:booking_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('payment/success/<int:booking_id>/', views.payment_success, name='payment_success'),
    path('payment/cancel/<int:booking_id>/', views.payment_cancel, name='payment_cancel'),
    path('stripe/webhook/', views.stripe_webhook, name='stripe_webhook'),

    path('car/<int:car_id>/feedback/', views.add_feedback, name='add_feedback'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),

    path('ajax/car_search/', views.ajax_car_search, name='ajax_car_search'),

    # Include DRF router urls
    path('', include(router.urls)),
]
