from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from couchdb import Server, ResourceNotFound
# from couchdb.client import ResourceNotFound

SERVER = Server('http://127.0.0.1:5984')
if len(SERVER) == 0:
    SERVER.create('docs')


def index(request):
    docs = SERVER['docs']
    if request.method == "POST":
        title = request.POST['title'].replace(' ', '')
        docs[title] = {'title': title, 'text': ""}
        return HttpResponseRedirect(u"/doc/%s/" % title)
    return render_to_response('demo/index.html', {'rows': docs})


def detail(request, id):
    docs = SERVER['docs']
    try:
        doc = docs[id]
    except:
        HttpResponseRedirect("bi loi")
    if request.method == "POST":
        doc['title'] = request.POST['title'].replace(' ', '')
        doc['text'] = request.POST['text']
        docs[id] = doc
    return render_to_response('demo/detail.html', {'row': doc})
