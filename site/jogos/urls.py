from django.conf.urls import url
from jogos.views import DiaSorteView

urlpatterns = [
    url(r'^dia_sorte$', DiaSorteView.as_view(), name='dia_sorte'),
]