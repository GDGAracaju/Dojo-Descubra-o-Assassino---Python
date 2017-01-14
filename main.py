# coding=utf8

import unittest

def existeNaLista(item,lista):
    list.index

def testarNumeros(assassino,local,arma):
    if (assassino == 5) and (local == 3) and (arma == 4):
        return True
    else:
        return False
        


############# teste ###############
class QuemMatouBillGTeste(unittest.TestCase):
    def teste1(self):
        self.assertEqual(True, testarNumeros(5,3,4))

    def teste2(self):
        self.assertEqual(False, testarNumeros(1,2,3))
    



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