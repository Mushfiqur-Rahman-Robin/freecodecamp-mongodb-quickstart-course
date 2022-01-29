import datetime
import mongoengine

from data.bookings import Booking


class Cage(mongoengine.Document):  # Top level document
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)

    name = mongoengine.StringField(required=True)
    price = mongoengine.FloatField(required=True)
    square_meters = mongoengine.FloatField(required=True)
    is_carpeted = mongoengine.BooleanField(required=True)
    has_toys = mongoengine.BooleanField(required=True)
    allow_dangerous_snakes = mongoengine.BooleanField(default=False)

    bookings = mongoengine.EmbeddedDocumentListField(Booking)  # List of embedded documents

    meta = {
        'db_alias': 'core',
        'collection': 'cages'
    }
