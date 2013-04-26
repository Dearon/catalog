from django.views.generic import ListView

from braces.views import JSONResponseMixin

from .models import Entry

class EntriesJSONView(JSONResponseMixin, ListView):
    model = Entry

    def get(self, request, *args, **kwargs):
        self.queryset = self.get_queryset()

        context_dict = {}
        for entry in self.queryset:
            context_dict[entry.pk] = {'name': entry.name, 'content': entry.content}

        return self.render_json_response(context_dict)
