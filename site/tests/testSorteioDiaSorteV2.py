from django.test import TestCase
from loteria.classes import SorteioDiaSorteV2Request, SorteioDiaSorteV2


class TestSorteioDiaSorteV2(TestCase):

    def test_sorteio_sem_fixo(self):
        request = SorteioDiaSorteV2Request()
        request.listaFixos = []
        request.listaQtdSorteaveis = [3, 2, 2]
        request.qtdJogos = 5

        sorteio = SorteioDiaSorteV2()
        sorteio.monta_resultados(request)

        self.assertEqual(5, len(sorteio.resultados))

    def test_sorteio_10_jogos(self):
        request = SorteioDiaSorteV2Request()
        request.listaFixos = [1, 11, 31]
        request.listaQtdSorteaveis = [3, 2, 2]
        request.qtdJogos = 10

        sorteio = SorteioDiaSorteV2()
        sorteio.monta_resultados(request)

        self.assertEqual(request.qtdJogos, len(sorteio.resultados))

    def test_sorteio_1_cada_linha(self):
        request = SorteioDiaSorteV2Request()
        request.listaFixos = [1, 11, 31]
        request.listaQtdSorteaveis = [3, 2, 2]
        request.qtdJogos = 5

        sorteio = SorteioDiaSorteV2()
        sorteio.monta_resultados(request)

        self.assertEqual(5, len(sorteio.resultados))

    def test_sorteio_2_em_linha(self):
        request = SorteioDiaSorteV2Request()
        request.listaFixos = [1, 4, 15]
        request.listaQtdSorteaveis = [3, 2, 2]
        request.qtdJogos = 5

        sorteio = SorteioDiaSorteV2()
        sorteio.monta_resultados(request)

        self.assertEqual(5, len(sorteio.resultados))

    def test_sorteio_3_em_linha(self):
        request = SorteioDiaSorteV2Request()
        request.listaFixos = [1, 4, 10]
        request.listaQtdSorteaveis = [3, 2, 2]
        request.qtdJogos = 5

        sorteio = SorteioDiaSorteV2()
        sorteio.monta_resultados(request)

        self.assertEqual(5, len(sorteio.resultados))