from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from loteria.classes import EscolhasDiaSorte, DezenaDiaSorte
import json


class DiaSorteView(View):
    template_name = 'dia_sorte.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def dia_sorte_sorteio(request):
    request_data = json.loads(request.body)
    fixo = request_data['fixo']
    escolhas_dia_sorte = EscolhasDiaSorte()
    escolhas_dia_sorte.fixo = DezenaDiaSorte(fixo)
    for dezena in request_data['sorteaveis']:
        escolhas_dia_sorte.sorteaveis.append(DezenaDiaSorte(dezena))

    escolhas_dia_sorte.numeroJogos = request_data['numero_jogos']
    escolhas_dia_sorte.monta_resultado()

    json_string = json.dumps(escolhas_dia_sorte.resultados)

    return HttpResponse(json_string, content_type='application/json')
