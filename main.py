# coding=utf8

import unittest
import random

def existeNaLista(item,lista):
    list.index

def testarNumeros(assassino,local,arma):
    retorno= [] 
    
    if (assassino != 5):
        retorno.append(1)

    if (local != 3):
        retorno.append(2)

    if (arma != 4):
        retorno.append(3)

    if len(retorno) > 0:
        return retorno[random.randrange(0, len(retorno))]
    else:
        return 0
   


############# teste ###############
class QuemMatouBillGTeste(unittest.TestCase):
    def teste1(self):
        self.assertEqual(0, testarNumeros(5,3,4))

    def teste2(self):
        self.assertEqual(1, testarNumeros(1,2,3))
    
    def testeParametro1Errado(self):
        self.assertEqual(1, testarNumeros(1,3,4))

    def testeParametro2Errado(self):
        self.assertEqual(2, testarNumeros(5,1,4))

    def testeParametro3Errado(self):
        self.assertEqual(3, testarNumeros(5,3,1))


#1,1,1 : 2
#1,2,1 : 2
#1,3,1 : 1
#2,3,1 : 3
#2,3,2 : 3
#2,3,3 : 3
#2,3,4 : 0

#5,3,4

if __name__ == '__main__':
    unittest.main()

'''Suspeitos:
    Charles B. Abbage
    Donald Duck Knuth
    Ada L. Ovelace
    Alan T. Uring
    Ivar J. Acobson
    Ras Mus Ler Dorf
Locais:
    Redmond
    Palo Alto
    San Francisco
    Tokio
    Restaurante no Fim do Universo
    São Paulo
    Cupertino
    Helsinki
    Maida Vale
    Toronto
Armas:
    Peixeira
    DynaTAC 8000X (o primeiro aparelho celular do mundo)
    Trezoitão
    Trebuchet
    Maça
    Gládio'''