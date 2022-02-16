# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:59:45 2022

@author: DISRCT
"""

import random

print("------------- BEM VINDO AO CASINO ROYALLE!!! -------------")

baralho = {'A♣': 1, '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7,
           'A♥': 1, '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7,
           'A♠': 1, '2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7,
           'A♦': 1, '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7,
           '8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 10, 'Q♣': 10, 'K♣': 10,
           '8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 10, 'Q♥': 10, 'K♥': 10,
           '8♠': 8, '9♠': 9, '10♠': 10, 'J♠': 10, 'Q♠': 10, 'K♠': 10,
           '8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 10, 'Q♦': 10, 'K♦': 10}

listaMao = []
listaBanca = []

soma_jogador = 0
soma_banca = 0
saldo = 500
dinheiroColocado = 0

#DEFINE CASTAS DO USUARIO
def defineCartasJogador():
    global saldo, listaMao, listaBanca, soma_jogador, soma_banca
    global dinheiroColocado
    for cartas, valor in baralho.items():
        aleatorias = random.choice(list(baralho))
        listaMao.append(aleatorias)
        soma_jogador = soma_jogador + baralho[aleatorias]
        break
    
#DEFINE CASTAS DA BANCA
def defineCartasBanca():
    global saldo, listaMao, listaBanca, soma_jogador, soma_banca
    global dinheiroColocado
    for cartas, valor in baralho.items():
        aleatorias = random.choice(list(baralho))
        listaBanca.append(aleatorias)
        soma_banca = soma_banca + baralho[aleatorias]
        break 
    
#ESCOLHA USUARIO
def comecaJogo():
    while True:
        global saldo, listaMao, listaBanca, soma_jogador, soma_banca
        global dinheiroColocado
        soma_jogador = 0
        escolhaUsuario = str(input("Tem certeza que quer jogar? (s/n): "))
        escolhaUsuario.lower()
        if escolhaUsuario == 's':
            print("Você tem R$", saldo)
            break
        elif escolhaUsuario == 'n':
            print("Bundao!")
            break

#VERIFICA VENCEDOR
def verifica():
    global saldo, listaMao, listaBanca, soma_jogador, soma_banca
    global dinheiroColocado
    
    if soma_jogador == 21:
        saldo += dinheiroColocado
        return 1
    elif soma_banca > 21:
        saldo += dinheiroColocado
        return 1
    elif soma_jogador > 21:
        saldo -= dinheiroColocado
        return 0
    elif soma_banca == 21:
        saldo -= dinheiroColocado
        return 0
    elif soma_jogador < 21 and soma_jogador > soma_banca:
        saldo += dinheiroColocado
        return 1
    elif soma_jogador < 21 and soma_jogador < soma_banca:
        saldo += dinheiroColocado
        return 1
    elif soma_jogador > soma_banca and soma_banca < 21:
        saldo -= dinheiroColocado
        return 0
    elif soma_jogador == soma_banca:
        return 2
    
#NOVA ESCOLHA USUARIO
def recomecaJogoDescontando():
    while True:
        global saldo, listaMao, listaBanca, soma_jogador, soma_banca
        global dinheiroColocado
        listaBanca = []
        listaMao = []
        soma_banca = 0
        soma_jogador = 0
        escolhaUsuario = str(input("Tem certeza que quer jogar? (s/n): "))
        escolhaUsuario.lower()
        if escolhaUsuario == 's':
            print("Você tem R$", saldo)
            if saldo == 0:
                return 0
            break
        elif escolhaUsuario == 'n':
            print("Parabens você vai para casa com R$", saldo)
            return 0
            break
        
#VALOR DA APOSTA
def valorAposta():
    while True:
        global saldo, listaMao, listaBanca, soma_jogador, soma_banca
        global dinheiroColocado
        dinheiroAposta = int(input("Quanto deseja apostar? "))
        dinheiroColocado = dinheiroAposta
        if dinheiroColocado <= 0:
            print("Não pode ser apostado R$0 ou menos!")
            continue
        elif dinheiroColocado > saldo:
            print("Você não tem todo esse dinheiro!")
            continue
        break

#MOSTRA SOMA E CARTAS DO JOGADOR
def mostraCartaJogador():
    global saldo, listaMao, listaBanca, soma_jogador, soma_banca
    global dinheiroColocado
    for i in range(2):
        defineCartasJogador()
    print("Suas cartas são:", listaMao, "soma:", soma_jogador)

#MOSTRA SOMA E CARTAS DA BANCA
def mostraCartaBanca():
    global saldo, listaMao, listaBanca, soma_jogador, soma_banca
    global dinheiroColocado
    
    for i in range(2):
        defineCartasBanca()
    print("Cartas da banca:", listaBanca[0])
    
#FAZER MAIS UM HIT
def fazerHit():
    global saldo, listaMao, listaBanca, soma_jogador, soma_banca
    global dinheiroColocado
    while soma_jogador < 21:
        
        hit = str(input("Deseja fazer mais um hit? (s/n) "))
        hit.lower()
        if hit == 's':
            defineCartasJogador()
            print("Suas cartas são:", listaMao, "soma:", soma_jogador)
        elif hit == 'n':
            for i in range(17):
                print("Jogo da banca:", listaBanca, "soma:", soma_banca)
                defineCartasBanca()
                if soma_banca > 17:
                    print("Jogo da banca:", listaBanca, "soma:", soma_banca)
                    break
            break
            
comecaJogo()

while True:
    valorAposta()
    mostraCartaJogador()
    mostraCartaBanca()
    fazerHit()    
    a = verifica()
    if a == 1:
        print("VOCÊ GANHOU!")
    elif a == 0:
        print("VOCÊ PERDEU!")
    elif a == 2:
        print("EMPATE!")
    
    control = recomecaJogoDescontando()
    if control == 0:
        break
    
