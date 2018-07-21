from django.conf.urls import url
from jogos.views import DiaSorteView, dia_sorte_sorteio

urlpatterns = [
    url(r'^dia_sorte$', DiaSorteView.as_view(), name='dia_sorte'),
    url(r'^dia_sorte_sorteio$', dia_sorte_sorteio, name='dia_sorte_sorteio'),
]