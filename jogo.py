import introducao


def iniciar_jogo():

    inicio = input("1 - Iniciar Jogo\n"
                   "2 - Sair\n"
                   "Escolha: ")
    if(inicio == "1"):
        print("Start")
        nome_jogador = input("Insira o nome do jogador: ")
        print()

        personagens = inicia_personagem()
        introducao.iniciar_introducao()
        decisoes()

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


def decisoes():
    print()
    print("Você está sentado em um mesa de uma taverna da capital, quando entra pela porta a princesa do reino.")
    print("Junto dela, 2 guarda com armaduras brilhantes e um servo com um pergaminho em mãos.")
    print("O servo enche o peito de ar e grita: ")
    print("- Apresento a vocês a Princesa Andromeda, ela possui uma missão muito importante para o aventureiro mais\n"
          " corajoso desse reino.")
    print("- O aventureiro que tiver interesse nessa missão, por favor, se levante e venha até nós")

    print("Qual sua escolha?")
    escolha = input("1 - Levantar e ir conversar com a Princesa Andromeda\n"
                    "2 - Atacar a Princesa Andromeda\n"
                    "Escolha: ")

    if(escolha == "1"):
        print("Você se levanta com um ar de glória e caminha em direção a Princesa.")
        print("A Princesa percebe você se aproximando e fala:")
        print("- Oh bravo aventureiro, está será um missão difícil.")
        print("- ")
    elif(escolha == "2"):
        print("Vecê se levanta com raiva, saca sua espada, e corre em direção a princesa.")
        print("Os guardas percebem sua ação e puxam a princesa para trás deles e formam um barreira de escudos.")
        print("Os cidadões da taverna se enfurecem e partem pra cima de você.")
        print("Você é morto pela população furiosa e pelos guardas da corte.")



if(__name__ == "__main__"):
    iniciar_jogo()