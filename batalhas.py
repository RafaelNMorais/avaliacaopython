import random

def batalha_bandido():
    hp_jogador = 100
    hp_inimigo = 100
    while (hp_jogador > 0 and hp_inimigo > 0):
        ataque_jogador = random.randrange(1, 21)
        ataque_inimigo = random.randrange(1, 16)
        hp_jogador = hp_jogador - ataque_inimigo
        hp_inimigo = hp_inimigo - ataque_jogador
        if (hp_inimigo < 0):
            hp_inimigo = 0
        elif (hp_jogador < 0):
            hp_jogador = 0
        print("Hp jogador = {}".format(hp_jogador))
        print(ataque_jogador)
        print("Hp inimigo = {}".format(hp_inimigo))
        print(ataque_inimigo)
        continua = input("1- Continua")

def batalha_artorias():
    hp_jogador = 100
    hp_inimigo = 100
    while(hp_jogador > 0 and hp_inimigo > 0):
        ataque_jogador = random.randrange(1,21)
        ataque_inimigo = random.randrange(1,21)
        hp_jogador = hp_jogador - ataque_inimigo
        hp_inimigo = hp_inimigo - ataque_jogador
        if (hp_inimigo < 0):
            hp_inimigo = 0
        elif (hp_jogador < 0):
            hp_jogador = 0
        print("Hp jogador = {}".format(hp_jogador))
        print(ataque_jogador)
        print("Hp inimigo = {}".format(hp_inimigo))
        print(ataque_inimigo)
        continua = input("1- Continua")

def batalha_marco():
    hp_jogador = 100
    hp_inimigo = 100
    while(hp_jogador > 0 and hp_inimigo > 0):
        ataque_jogador = random.randrange(1, 21)
        ataque_inimigo = random.randrange(1, 21)
        hp_jogador = hp_jogador - ataque_inimigo
        hp_inimigo = hp_inimigo - ataque_jogador
        if (hp_inimigo < 0):
            hp_inimigo = 0
        elif (hp_jogador < 0):
            hp_jogador = 0
        print("Hp jogador = {}".format(hp_jogador))
        print(ataque_jogador)
        print("Hp inimigo = {}".format(hp_inimigo))
        print(ataque_inimigo)
        continua = input("1- Continua")

def batalha_velazar():
    hp_jogador = 100
    hp_inimigo = 100
    while(hp_jogador > 0 and hp_inimigo > 0):
        ataque_jogador = random.randrange(1, 21)
        ataque_inimigo = random.randrange(1, 21)
        hp_jogador = hp_jogador - ataque_inimigo
        hp_inimigo = hp_inimigo - ataque_jogador
        if (hp_jogador < 0):
            hp_jogador = 0
        elif (hp_inimigo < 0):
            hp_inimigo = 0
        print("Hp jogador = {}".format(hp_jogador))
        print(ataque_jogador)
        print("Hp inimigo = {}".format(hp_inimigo))
        print(ataque_inimigo)
        continua = input("1- Continua")