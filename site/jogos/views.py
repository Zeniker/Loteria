from django.views import View
from django.shortcuts import render

# Create your views here.


class DiaSorteView(View):
    template_name = 'dia_sorte.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
