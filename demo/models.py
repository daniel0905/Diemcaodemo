from datetime import datetime
from couchdbkit.ext.django.schema import *


class Greeting(Document):
    author = StringProperty()
    content = StringProperty(required=True)
    date = DateTimeProperty(default=datetime.now())
