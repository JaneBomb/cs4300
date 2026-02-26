from django.core.management.base import BaseCommand
from datetime import date, timedelta
from bookings.models import Movie

class Command(BaseCommand):
    help = "adds movies to the database (minaly for testing so it's not blank)"
    def handle(self, *args, **kwargs):
        '''
        FOR TESTING
        Populates the movie database
        '''
        movies = [
            Movie(title="Movie 1", description="1 Description", release_date=date(26, 1, 1), duration=timedelta(hours=1, minutes=30)),
            Movie (title="Movie 2", description="2 Description", release_date=date(26, 2, 2), duration=timedelta(hours=2, minutes=30))
        ]
        Movie.objects.bulk_create(movies)                                        # Recurses through movies list and adds Movie
        self.stdout.write(self.style.SUCCESS("Movies added successfully!"))         # TESTING