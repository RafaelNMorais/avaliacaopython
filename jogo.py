import introducao


def iniciar_jogo():

    inicio = input("[1] - Iniciar Jogo\n"
                   "[2] - Sair\n"
                   "Escolha: ")
    if(inicio == "1"):
        print("Start")
        nome_jogador = input("Insira o nome do jogador: ")
        print()

        personagens = inicia_personagem()
        introducao.iniciar_introducao()
        decisoes1()

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
    personagem5 = personagens[4]
    personagem6 = personagens[6]

    return personagem1, personagem2, personagem3, personagem4, personagem5, personagem6


def decisoes1():
    print()
    print("Você está sentado em um mesa de uma taverna da capital, quando entra pela porta a princesa do reino.")
    print("Junto dela, 2 guarda com armaduras brilhantes e um servo com um pergaminho em mãos.")
    print("O servo enche o peito de ar e grita: ")
    print("- Apresento a vocês a Princesa Andromeda, ela possui uma missão muito importante para o aventureiro mais\n"
          " corajoso desse reino.")
    print("- O aventureiro que tiver interesse nessa missão, por favor, se levante e venha até nós")

    print("Qual sua escolha?")
    escolha = input("[1] - Levantar e ir conversar com a Princesa Andromeda\n"
                    "[2] - Atacar a Princesa Andromeda\n"
                    "Escolha: ")

    if(escolha == "1"):
        print()
        print("Você se levanta com um ar de glória e caminha em direção a Princesa.")
        print("A Princesa percebe você se aproximando e fala:")
        print("- Oh bravo aventureiro, está será um missão difícil.")
        print("- Você deverá ir até o Obelisco do Espaço resgatar o Mestre dos Magos.")
        print("- Ele foi raptado por um Ninja poderoso.")
        print("- Você deve seguir ao Norte até encontrar a Gruta de Drayhill.")
        print("- Ela é protegida pelo temido Marco Nove Vidas.")
        print("- Tenha cuidado guerreiro, que seu caminho seja ilumidado.")
        decisoes2()
    elif(escolha == "2"):
        print()
        print("Vecê se levanta com raiva, saca sua espada, e corre em direção a princesa.")
        print("Os guardas percebem sua ação e puxam a princesa para trás deles e formam um barreira de escudos.")
        print("Os cidadões da taverna se enfurecem e partem pra cima de você.")
        print("Você é morto pela população furiosa e pelos guardas da corte.")


def decisoes2():
    print()
    print("Você sai pela porta da taverna, se depara com a praça da cidade, ela está lotada de moradores e comerciantes")
    print("Segue em frente pela portão principal, quando um guarda te para e fala:")
    print("- Ei você ai, você é o maluco que aceitou a missão da Princesa?")
    print("- Ah você tem culhões amigo...")
    print("- Espere um momento ai, quero te contar uma coisa...")
    escolha1 = input("[1] - Continuar andando e ignorar o guarda\n"
                     "[2] - Parar e ouvir o conselho do guarda\n"
                     "Escolha: ")
    if(escolha1 == "1"):
        print()
        print("Você segue andando pela estrada sem se importar com o guarda.")
        print("Enquanto isso o guarda te olha de longe com um rosto de preocupação.")
        print()
    elif(escolha1 == "2"):
        print()
        print("Você para ao lado do guarda e ele te fala:")
        print("- Seguinte amigo, para chegar até a Gruta de Drayhill você tem dois caminhos.")
        print("- Você pode seguir pela estrada principal, onde os únicos perigos serão simples bandidos.")
        print("- Ou ir pela Floresta de Durgamau, onde o temido Artorias se encontra.")
        print("- Pela estrada você levará muito mais tempo para chegar no destino, mas será mais seguro.")
        print("- Já pela floresta chegará rapidamente a gruta, mas com o perigo sempre a espreita.")
        print("- Escolha sabiamente seu caminho.")
        print()
    decisoes3()


def decisoes3():
    print()
    escolha3 = input("[1] - Seguir o caminho pela estrada\n"
                     "[2] - Seguir o caminho pela floresta")
    if(escolha3 == "1"):
        print()
        print("Você caminha pela estrada, ela é bem populada, passa por alguns comerciantes e fazendeiros.")
        print("Já estava na caida da noite, a estrada começa a ficar vazia, tudo está escuro ao seu redor.")
        print("Há alguns postes com lampiões pendurados iluminado o caminho.")
        print("Falta só alguns quilometros para a entrada da gruta.")
        print("Você começa a escutar barulhos vindo do mato qua tem ao lado da estrada.")
        print("Pode ser só um animal, como também pode ser um bandido escondido.")
        print()
        escolha4 = input("[1] - Investigar o barulho no mato\n"
                         "[2] - Ignorar o barulho e seguir em frente\n"
                         "Escolha: ")
        if(escolha4 == "1"):
            print()

        elif(escolha4 == "2"):
            print()
    elif(escolha3 == "2"):
        print()


if(__name__ == "__main__"):
    iniciar_jogo()