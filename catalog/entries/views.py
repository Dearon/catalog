from django.views.generic import TemplateView, ListView, View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie

from braces.views import JSONResponseMixin

from .models import Entry

class EntriesHomeView(TemplateView):
    template_name = 'home.html'

    @method_decorator(ensure_csrf_cookie)
    def get(self, request, *args, **kwargs):
        return super(EntriesHomeView, self).get(request, *args, **kwargs)

class EntriesView(JSONResponseMixin, ListView):
    model = Entry

    def get(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()

        context_list = list()
        for entry in self.queryset:
            context_list.append({'id': entry.pk, 'name': entry.name, 'content': entry.content})

        return self.render_json_response(context_list)

class AddEntryView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context_dict = {'success': 'false'}
        return self.render_json_response(context_dict)

    def post(self, request, *args, **kwargs):
        entry = Entry(name=request.POST['name'], content=request.POST['content'])
        entry.save()

        context_dict = {
            'success': 'true',
            'id': entry.pk,
            'name': entry.name,
            'content': entry.content
        }
        
        return self.render_json_response(context_dict)

class EditEntryView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context_dict = {'success': 'false'}
        return self.render_json_response(context_dict)

    def post(self, request, *args, **kwargs):
        entry = Entry.objects.get(pk=request.POST['id'])
        entry.name = request.POST['name']
        entry.content = request.POST['content']
        entry.save()

        context_dict = {
            'success': 'true',
            'name': entry.name,
            'content': entry.content
        }

        return self.render_json_response(context_dict)

class RemoveEntryView(JSONResponseMixin, View):
    def get(self, request, *args, **kwargs):
        context_dict = {'success': 'false'}
        return self.render_json_response(context_dict)

    def post(self, request, *args, **kwargs):
        entry = Entry.objects.get(pk=request.POST['id'])
        entry.delete()

        context_dict = {
            'success': 'true',
        }
        
        return self.render_json_response(context_dict)
