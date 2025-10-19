from rest_framework import viewsets
from rest_framework import permissions
from .models import Listing, Booking
from .serializers import BookingListSerializer, PropertyListingSerializer

# Create your views here.
class ListingViewSet(viewsets.ModelViewSet):
    """
    CRUD for Listings
    GET /api/listings/
    POST /api/listings/
    GET /api/listings/{id}/
    PUT/PATCH /api/listings/{id}/
    DELETE /api/listings/{id}/
    """
    queryset = Listing.objects.all().order_by("-id")
    serializer_class = PropertyListingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        # If Listings are owned, wire this up (safe if there's no owner field)
        serializer.save(owner=getattr(self.request, "user", None))
        
class BookingViewSet(viewsets.ModelViewSet):
    """
    CRUD for Bookings
    GET /api/bookings/
    POST /api/bookings/
    GET /api/bookings/{id}/
    PUT/PATCH /api/bookings/{id}/
    DELETE /api/bookings/{id}/
    """
    queryset = Booking.objects.all().order_by("-id")
    serializer_class = BookingListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(user=getattr(self.request, "user", None))        
