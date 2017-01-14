# coding=utf8

import unittest


def testeAssassino(assassino):
    if assassino == 5:
        return True
    else:
        return False

def testeLocal(local):
    if local == 3:
        return True
    else:
        return False

def testeArma(arma):
    if arma == 4:
        return True
    else:
        return False

def testarNumeros(assassino,local,arma):
    
    # o resulto certo eh 5,3,4
    return testeAssassino(assassino) and testeLocal(local) and testeArma(arma)
    

        


############# teste ###############
class QuemMatouBillGTeste(unittest.TestCase):
    def teste1(self):
        self.assertEqual(True, testarNumeros(5,3,4))



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