from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

# creates an URL for bookings
urlpatterns = [
    path('movies/', views.test_base, name='bookings'),
    #path('seats/', views.seats_list),
    
    #path('create/', views.BookingsListCreateAPIView.as_view(), name='create-bookings'),
    #path('user-bookings/', views.UserBookingListAPIView.as_view(), name='user-bookings'),
]
 
router = DefaultRouter()
router.register('create', views.BookingsViewSet)
urlpatterns += router.urls