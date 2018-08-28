from django.conf.urls import url
from jogos.views import DiaSorteV1View, DiaSorteV2View, dia_sorte_sorteio

urlpatterns = [
    url(r'^dia_sorte_v1$', DiaSorteV1View.as_view(), name='dia_sorte_v1'),
    url(r'^dia_sorte_v1_sorteio$', dia_sorte_sorteio, name='dia_sorte_v1_sorteio'),

    url(r'^dia_sorte_v2$', DiaSorteV2View.as_view(), name='dia_sorte_v2'),
]