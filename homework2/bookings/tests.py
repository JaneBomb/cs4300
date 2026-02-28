from django.test import TestCase
from datetime import date
from bookings.models import Booking
from django.urls import reverse

from django.contrib.auth.models import User
from rest_framework import status

# Create your tests here.
class UserBookingTestCase(TestCase):
    def setUp(self):
        '''
        Creates objects in the API(s) for testing
        Temporary objects
        '''
        user1 = User.objects.create_user(username='Alice', password='test')
        user2 = User.objects.create_user(username='Bob', password='test')
        Booking.objects.create(movie='Movie1', seat=1, user=user1, booking_date=date(2026, 1, 1))
        Booking.objects.create(movie='Movie1', seat=5, user=user1, booking_date=date(2027, 2,14))
        Booking.objects.create(movie='Movie1', seat=4, user=user2, booking_date=date(2026, 1, 1))

    def test_user_booking_endpoint_only_retrieves_authenticated_user_bookings(self):
        '''
        Tests to see if the correct bookings are shown based on username/user
        '''
        user = User.objects.get(username='Alice')               #Change string based on user checking
        self.client.force_login(user)
        response = self.client.get(reverse('user-bookings'))

        assert response.status_code == status.HTTP_200_OK
        bookings = response.json()
        self.assertTrue(all(booking['user'] == user.id for booking in bookings) )

    def test_user_booking_unauthenticated_user(self):
        '''
        Tests if the 403 (unauthenticated user) error code is used, when there is no authenticated user
        Ensures only users can see their own bookings
        '''
        response = self.client.get(reverse('user-bookings'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)