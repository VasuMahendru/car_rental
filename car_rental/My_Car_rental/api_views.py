# rental/api_views.py

from rest_framework import viewsets, permissions
from .models import Car, Booking, Feedback
from .serializers import CarSerializer, BookingSerializer, FeedbackSerializer
from rest_framework.permissions import IsAuthenticated

class CarViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.AllowAny]

class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Booking.objects.all()
        return Booking.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Feedback.objects.all()  # Allow read of all feedbacks

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
