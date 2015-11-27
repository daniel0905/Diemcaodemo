from couchdbkit import Server
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, DeleteView
from demo.forms import GreetingForm
from demo.models import Greeting


class CreateViewGreeting(CreateView):
    model = Greeting
    form_class = GreetingForm
    template_name = 'demo/home.html'

    def form_valid(self, form):
        form.save()
        return HttpResponse('thanh cong')


class ListViewGreet(ListView):
    model = Greeting
    paginate_by = 2
    template_name = 'demo/greet_list.html'

    def get_queryset(self):

        cmd = list(Greeting.view('demo/all'))
        a = []
        for x in cmd:
            a.append(x['key'])
        return a


class DeleteViewGreet(DeleteView):
    model = Greeting

    def delete(self, request, *args, **kwargs):
        server = Server()
        db = server['demo']
        id = request.POST.get('id')
        cmd = 'function(doc){if (doc.author == ' + id + ') {emit(null, doc._deleted'
        self.object.filter(id=id).delete()
        return HttpResponse("thanh cong")