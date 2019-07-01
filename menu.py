def iniciar_jogo():

    inicio = input("[1] - Iniciar Jogo\n"
                   "[2] - Sair")
    if(inicio == "1"):
        print("Start")
        nome_jogador1 = input("Insira o nome do jogador 1")

        personagens = inicia_personagem()

    elif(inicio == "2"):
        print("Encerrando")

def inicia_personagem():
    arquivo = open("personagens.txt", "r")
    personagens = []

    for linha in arquivo:
        linha = linha.strip()
        personagens.append(linha)

    arquivo.close

    personagem1 = personagens[0]
    personagem2 = personagens[1]
    personagem3 = personagens[2]
    personagem4 = personagens[3]

    return personagem1, personagem2, personagem3, personagem4


if(__name__ == "__main__"):
    iniciar_jogo()