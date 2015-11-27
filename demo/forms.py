from couchdbkit.ext.django.forms import DocumentForm
from demo.models import Greeting


class GreetingForm(DocumentForm):
    class Meta:
        document = Greeting
