import math
import random


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
# blau
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