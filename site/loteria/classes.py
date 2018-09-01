import math
import random


class Sorteador(object):
    def sorteia_indice(self, min, max):
        if min != max:
            return random.randint(min, max-1)
        else:
            return min


class DezenaDiaSorte(object):
    def __init__(self, dicionario):
        self.numero = dicionario['numero']
        self.quant_sorteado = 0


class EscolhasDiaSorte(object):
    def __init__(self):
        self.fixo = None
        self.sorteaveis = []
        self.resultados = []
        self.numeroJogos = 0
        self.blau = 0

    def monta_resultado(self):
        maximo_repeticao = math.floor((self.numeroJogos * 60) / 100)
        for i in range(self.numeroJogos):
            self.resultados.append([])

        # indice_resultados = 0
        sorteaveis_jogo = self.sorteaveis.copy()
        proximos_sorteaveis = []

        for resultado in self.resultados:
            resultado.append(self.fixo.numero)
            while len(resultado) < 7:
                indice_sorteado = self._sorteia_indice(0, len(sorteaveis_jogo))
                resultado.append(sorteaveis_jogo[indice_sorteado].numero)
                dezena_sorteada = sorteaveis_jogo.pop(indice_sorteado)
                dezena_sorteada.quant_sorteado += 1
                # print(str(dezena_sorteada.numero) + ' ' + str(dezena_sorteada.quant_sorteado))
                if dezena_sorteada.quant_sorteado < maximo_repeticao:
                    proximos_sorteaveis.append(dezena_sorteada)

                if len(sorteaveis_jogo) == 0:
                    sorteaveis_jogo = proximos_sorteaveis.copy()
                    # print(len(sorteaveis_jogo))
                    proximos_sorteaveis = []

                # indice_geral = self._get_indice_sorteaveis(sorteaveis_jogo[indice_sorteado])
                #
                # print(self.sorteaveis[indice_geral].numero)
                # self.sorteaveis[indice_geral].quant_sorteado += 1
                # if self.sorteaveis[indice_geral].quant_sorteado > 2:
                #     self.sorteaveis.pop(indice_geral)

            resultado.sort()

    def _sorteia_indice(self, min, max):
        if min != max:
            return random.randint(min, max-1)
        else:
            return min

    def _get_indice_sorteaveis(self, dezena):
        indice = 0
        while indice < len(self.sorteaveis):
            if self.sorteaveis[indice].numero == dezena.numero:
                return indice
            indice += 1

        return 0


class SorteioDiaSorteV2Request(object):
    def __init__(self):
        self.listaFixos = []
        self.listaQtdSorteaveis = []
        self.qtdJogos = 0


class SorteioDiaSorteV2(object):
    def __init__(self):
        self.sorteaveisLinha = []
        self.sorteaveisLinha.append(list(range(1, 11)))
        self.sorteaveisLinha.append(list(range(11, 21)))
        self.sorteaveisLinha.append(list(range(21, 32)))
        self.resultados = []
        self.request = SorteioDiaSorteV2Request()
        self.sorteador = Sorteador()

    def monta_resultados(self, request: SorteioDiaSorteV2Request):
        self.request = request

        for indice in range(0, self.request.qtdJogos):
            resultado = []
            igual_antigo = False
            self._insere_numeros_fixos_resultado(resultado)
            self._sorteia_jogo(resultado)
            resultado.sort()
            for resultado_antigo in self.resultados:
                if resultado_antigo == resultado:
                    igual_antigo = True
            if not igual_antigo:
                self.resultados.append(resultado)

        # self._print_resultados()

    def _sorteia_jogo(self, resultado: list):
        for indice_linha, linha in enumerate(self.sorteaveisLinha):
            max_sorteio_linha = self.request.listaQtdSorteaveis[indice_linha]
            sorteaveis = linha.copy()
            qtd_removidos = self._remove_fixos_sorteaveis(sorteaveis)
            qtd_sorteados = 0
            max_sorteio_linha = max_sorteio_linha - qtd_removidos

            while qtd_sorteados < max_sorteio_linha:
                indice_sorteado = self.sorteador.sorteia_indice(0, len(sorteaveis))
                resultado.append(sorteaveis[indice_sorteado])
                sorteaveis.pop(indice_sorteado)
                qtd_sorteados += 1

    def _insere_numeros_fixos_resultado(self, resultado: list):
        for fixo in self.request.listaFixos:
            resultado.append(fixo)

    def _remove_fixos_sorteaveis(self, sorteaveis: list):
        qtd_removidos = 0
        for fixo in self.request.listaFixos:
            if fixo in sorteaveis:
                indice_fixo = sorteaveis.index(fixo)
                sorteaveis.pop(indice_fixo)
                qtd_removidos += 1

        return qtd_removidos

    def _print_resultados(self):
        print('---------------------------------')
        for resultado in self.resultados:
            print(resultado)
