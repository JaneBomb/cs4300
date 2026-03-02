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
            Movie(
                title="Toy Story", 
                description="A cowboy doll is profoundly jealous when a new spaceman action figure supplants him as the top toy in a boy's bedroom. When circumstances separate them from their owner, the duo have to put aside their differences to return to him.",
                release_date=date(1995, 11, 22),
                duration=timedelta(hours=1, minutes=21)
            ),
            Movie (
                title="Toy Story 2",
                description="When Woody is stolen by a toy collector, Buzz and his friends set out on a rescue mission to save Woody before he becomes a museum toy property with his roundup gang Jessie, Prospector, and Bullseye.",
                release_date=date(1999, 11, 24),
                duration=timedelta(hours=1, minutes=32)
            ),
            Movie (
                title="Toy Story 3",
                description="The toys are mistakenly delivered to a day-care center instead of the attic right before Andy leaves for college, and it's up to Woody to convince the other toys that they weren't abandoned and to return home.",
                release_date=date(2010, 6, 18),
                duration=timedelta(hours=1, minutes=43)
            ),
            Movie (
                title="Toy Story 4",
                description="When Woody, Buzz, and the gang join Bonnie on a road trip with her new craft project turned toy, Forky, the innocent little spork's antics launch Woody on a wild quest.",
                release_date=date(2019, 6, 21),
                duration=timedelta(hours=1, minutes=40)
            ),
        ]
        Movie.objects.bulk_create(movies)                                        # Recurses through movies list and adds Movie
        self.stdout.write(self.style.SUCCESS("Movies added successfully!"))         # TESTING