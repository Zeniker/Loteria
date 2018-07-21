import math


class DezenaDiaSorte(object):
    def __init__(self, dicionario):
        self.numero = dicionario['numero']
        self.quant_sorteado = dicionario['quant_sorteado']


class EscolhasDiaSorte(object):
    def __init__(self):
        self.fixo = None
        self.sorteaveis = []
        self.resultados = []
        self.numeroJogos = 0
        self.maximoRepeticao = 0
        self.blau = 0

    def monta_resultado(self):
        self.maximoRepeticao = math.floor((self.numeroJogos * 60) / 100)
        for i in range(self.numeroJogos):
            self.resultados.append([])

        indice_resultados = 0

        for dezena in self.sorteaveis:
            i = 0
            while i < self.maximoRepeticao:
                self.resultados[indice_resultados].append(dezena.numero)
                i += 1
                indice_resultados += 1
                if indice_resultados > len(self.resultados) - 1:
                    indice_resultados = 0
        for resultado in self.resultados:
            resultado.append(self.fixo.numero)


