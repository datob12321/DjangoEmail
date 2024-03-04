from django.shortcuts import render

class ObjectMixin:
    model = None
    template = None

    def get(self, request):
        objs = self.model.objects.all()
        return render(request, self.template, context={self.model.__name__.lower(): objs})
