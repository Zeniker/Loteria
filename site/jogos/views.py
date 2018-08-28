from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from loteria.classes import EscolhasDiaSorte, DezenaDiaSorte, SorteioDiaSorteV2
import json


class DiaSorteV1View(View):
    template_name = 'dia_sorte_v1.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class DiaSorteV2View(View):
    template_name = 'dia_sorte_v2.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def dia_sorte_sorteio_v1(request):
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


def dia_sorte_sorteio_v2(request):
    request_data = json.loads(request.body)
    lista_valores = request_data['listaValores']
    sorteio_dia_sorte = SorteioDiaSorteV2()

    sorteio_dia_sorte.monta_resultado(lista_valores)

    # json_string = json.dumps(sorteio_dia_sorte)

    return HttpResponse("", content_type='application/json')
