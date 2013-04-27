from django.views.generic import ListView, View

from braces.views import JSONResponseMixin

from .models import Entry

class EntriesJSONView(JSONResponseMixin, ListView):
    model = Entry

    def get(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()

        context_dict = {}
        for entry in self.queryset:
            context_dict[entry.pk] = {'id': entry.pk, 'name': entry.name, 'content': entry.content}

        return self.render_json_response(context_dict)

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
