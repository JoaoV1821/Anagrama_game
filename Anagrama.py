from random import sample

class Anagrama:
    def __init__(self):
        self.__tentativas = 5
        self.__dic_palavras = self.__embaralha_palavra()
        self.__palavra_sorteada = self.sorteia(self.__dic_palavras)
        self.__palavra_embaralhada = self.__palavra_sorteada[0][1]
        self.__palavra_normal = self.__palavra_sorteada[0][0]
    

    @staticmethod
    def __embaralha_palavra():
        
        palavras = {}

        with open('palavras.csv', mode='r', encoding='UTF-8') as arquivo:
            for palavra in arquivo.readlines():
                palavra = palavra.replace('\n', '')
                palavras[palavra] = ''.join(sample(palavra, len(palavra)))
        return palavras
    

    @staticmethod
    def sorteia(dict):
        return sample(dict.items(), 1)


    @property
    def tentativas(self):
        return self.__tentativas


    @property
    def palavra_embaralhada(self):
        return self.__palavra_embaralhada


    @property
    def palavra_normal(self):
        return self.__palavra_normal


    @tentativas.setter
    def tentativas(self, value):
        self.__tentativas = value
