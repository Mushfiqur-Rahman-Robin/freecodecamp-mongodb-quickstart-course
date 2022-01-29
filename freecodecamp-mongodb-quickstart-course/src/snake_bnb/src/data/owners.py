import datetime
import mongoengine


class Owner(mongoengine.Document):  # Top level document
    registered_date = mongoengine.DateTimeField(default=datetime.datetime.now)
    name = mongoengine.StringField(required=True)
    email = mongoengine.StringField(required=True)

    snake_ids = mongoengine.ListField()  # stores object ids referred to snake
    cage_ids = mongoengine.ListField()  # stores object ids referred to cage

    meta = {
        'db_alias': 'core',
        'collection': 'owners'
    }
