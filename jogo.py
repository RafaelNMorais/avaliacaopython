import introducao
import batalhas
import sys


def iniciar_jogo():
    inicio_str = input("[1] - Iniciar Jogo\n"
                       "[2] - Sair\n"
                       "Escolha: ")
    inicio = int(inicio_str)
    if (inicio == 1):
        introducao.iniciar_introducao()
        print()
        nome_jogador = input("Insira o nome do jogador: \n")
        print()

        personagens = inicia_personagem()
        decisoes1()

    elif (inicio == 2):
        print("  ⠄⠄⠄⠄⠄⠄⣀⣀⣀⣤⣶⣿⣿⣶⣶⣶⣤⣄⣠⣴⣶⣿⣿⣿⣿⣶⣦⣄⠄⠄\n"
                "⠄⠄⣠⣴⣾⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦\n"
                "⢠⠾⣋⣭⣄⡀⠄⠄⠈⠙⠻⣿⣿⡿⠛⠋⠉⠉⠉⠙⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⡎⣾⡟⢻⣿⣷⠄⠄⠄⠄⠄⡼⣡⣾⣿⣿⣦⠄⠄⠄⠄⠄⠈⠛⢿⣿⣿⣿⣿⣿\n"
                "⡇⢿⣷⣾⣿⠟⠄⠄⠄⠄⢰⠁⣿⣇⣸⣿⣿⠄⠄⠄⠄⠄⠄⠄⣠⣼⣿⣿⣿⣿\n"
                "⢸⣦⣭⣭⣄⣤⣤⣤⣴⣶⣿⣧⡘⠻⠛⠛⠁⠄⠄⠄⠄⣀⣴⣿⣿⣿⣿⣿⣿⣿\n"
                "⠄⢉⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣦⣶⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⢰⡿⠛⠛⠛⠛⠻⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⠸⡇⠄⠄⢀⣀⣀⠄⠄⠄⠄⠄⠉⠉⠛⠛⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⠄⠈⣆⠄⠄⢿⣿⣿⣿⣷⣶⣶⣤⣤⣀⣀⡀⠄⠄⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⠄⠄⣿⡀⠄⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠄⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⠄⠄⣿⡇⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠄⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⠄⠄⣿⡇⠄⠠⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n"
                "⠄⠄⣿⠁⠄⠐⠛⠛⠛⠛⠉⠉⠉⠉⠄⠄⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿\n"
                "⠄⠄⠻⣦⣀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠄")


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
    personagem6 = personagens[5]

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
    escolha_str = input("[1] - Levantar e ir conversar com a Princesa Andromeda\n"
                        "[2] - Atacar a Princesa Andromeda\n"
                        "Escolha: ")

    escolha = int(escolha_str)

    if (escolha == 1):
        print()
        print("Você se levanta com um ar de glória e caminha em direção a Princesa.")
        print("A Princesa percebe você se aproximando e fala:")
        print("- Oh bravo aventureiro, está será um missão difícil.")
        print("- Você deverá ir até o Obelisco do Espaço resgatar Ilenor o Mago da corte.")
        print("- Ele foi raptado por um Ninja poderoso.")
        print("- Você deve seguir ao Norte até encontrar a Gruta de Drayhill.")
        print("- Ela é protegida pelo temido Marco Nove Vidas.")
        print("- Tenha cuidado guerreiro, que seu caminho seja ilumidado.")
        decisoes2()
    elif (escolha == 2):
        print()
        print("Vecê se levanta com raiva, saca sua espada, e corre em direção a princesa.")
        print("Os guardas percebem sua ação e puxam a princesa para trás deles e formam um barreira de escudos.")
        print("Os cidadões da taverna se enfurecem e partem pra cima de você.")
        print("Você é morto pela população furiosa e pelos guardas da corte.")


def decisoes2():
    print()
    print(
        "Você sai pela porta da taverna, se depara com a praça da cidade, ela está lotada de moradores e comerciantes")
    print("Segue em frente pela portão principal, quando um guarda te para e fala:")
    print("- Ei você ai, você é o maluco que aceitou a missão da Princesa?")
    print("- Ah você tem culhões amigo...")
    print("- Espere um momento ai, quero te contar uma coisa...")
    escolha1_str = input("[1] - Continuar andando e ignorar o guarda\n"
                         "[2] - Parar e ouvir o conselho do guarda\n"
                         "Escolha: ")

    escolha1 = int(escolha1_str)

    if (escolha1 == 1):
        print()
        print("Você segue andando pela estrada sem se importar com o guarda.")
        print("Enquanto isso o guarda te olha de longe com um rosto de preocupação.")
        print()
    elif (escolha1 == 2):
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
    print("Como você morou na cidade a vida toda, acaba tendo o conhecimento que, para chegar a Gruta de Drayhill"
          " há dois caminhos a seguir: ")
    print()
    escolha3_str = input("[1] - Seguir o caminho pela estrada\n"
                         "[2] - Seguir o caminho pela floresta\n"
                         "Escolha: ")
    escolha3 = int(escolha3_str)
    if (escolha3 == 1):
        print()
        print("Você caminha pela estrada, ela é bem populada, passa por alguns comerciantes e fazendeiros.")
        print("Já estava na caida da noite, a estrada começa a ficar vazia, tudo está escuro ao seu redor.")
        print("Há alguns postes com lampiões pendurados iluminado o caminho.")
        print("Falta só alguns quilometros para a entrada da gruta.")
        print("Você começa a escutar barulhos vindo do mato qua tem ao lado da estrada.")
        print("Pode ser só um animal, como também pode ser um bandido escondido.")
        print()
        escolha4_str = input("[1] - Investigar o barulho no mato\n"
                             "[2] - Ignorar o barulho e seguir em frente\n"
                             "Escolha: ")
        escolha4 = int(escolha4_str)
        if (escolha4 == 1):
            print()
            print("Você se aproxima com cuidado do canto da estrada, vai afastando a grama alta com a mãos...")
            print("De repente um bandido pula em sua direção... e fala:")
            print("- Olha só oq eu encontrei por aqui, um engomadinho bisbilhoteiro...")
            print("Ele te ameaça com uma espada curta empunhada.")
            print("- É melhor ir passando suas coisas se não quiser problemas...")
            escolha5_str = input("[1] - Empunhar sua espada e lutar com o bandido.\n"
                                 "[2] - Empurar o bandido e correr pela estrada.\n"
                                 "Escolha: ")
            escolha5 = int(escolha5_str)
            if (escolha5 == 1):
                batalhas.batalha_bandido()
            elif (escolha5 == 2):
                print()
                print("Você empurra o bandido que caiu sentado no chão...")
                print("Você sai correndo e o bandido fica sem entender oque aconteceu...")
                print("Você corre pela estrada em direção a Gruta de Drayhill")
            print()
        elif (escolha4 == 2):
            print()
            print("Você acaba ficando assustado e acelera o passo, mas isso não foi o suficiente...")
            print("O barulho começa a te seguir e ficar cada vez mais alto...")
            print("Um bandido sai correndo do mato e para na sua frente...")
            print("Com um olher ameaçador ele fala:")
            print("- Ora ora oque temos aqui, um covarde querendo fugir da encrenca...")
            print("- Já que o amigo aqui está com pressa, passe as suas coisas pra cá, se não quiser problemas...")
            escolha6_str = input("[1] - Empunhar sua espada e lutar com o bandido.\n"
                                 "[2] - Empurar o bandido e correr pela estrada.\n"
                                 "Escolha: ")
            escolha6 = int(escolha6_str)
            if (escolha6 == 1):
                print()
                batalhas.batalha_bandido()
            elif (escolha6 == 2):
                print()
                print("Você empurra o bandido que caiu sentado no chão...")
                print("Você sai correndo e o bandido fica sem entender oque aconteceu...")
                print("Você corre pela estrada em direção a Gruta de Drayhill")
            print()
    elif (escolha3 == 2):
        print()
        print("Logo após sair da cidade você começa a adentrar na floresta.")
        print("O mato é denso e é preciso andar com cuidado. Uma névoa comaça a surgir estranhamente.")
        print("Quanto mais adentra a floresta, mais densa a névoa vai ficando.")
        print("Barulhos estranhos são ouvidos ao longe, uivos de lobos, gritos de corvos...")
        print("Sons de passos pesados se aproximam...")
        print(
            "A névoa começa a sumir, a floresta começa a ficar quieta, só se ouve os sons de passos se aproximando...")
        print("A névoa some por completo, revelando um cavaleiro com aramdura pesada...")
        print("Ele te encara, não fala uma palavra... Em sua mão empunha uma espada grande...")
        print("Você sente uma sensação estranha, como se a morte lhe desse um aperto de mão...")
        print("O cavaleiro começa a andar lentamente em sua direção...")
        print()
        escolha7_str = input("[1] - Empunhar a espada e atacar o cavaleiro.\n"
                             "[2] - Sair correndo pela sua vida.\n"
                             "Escolha: ")
        escolha7 = int(escolha7_str)
        print()
        if (escolha7 == 1):
            print()
            batalhas.batalha_artorias()
        elif (escolha7 == 2):
            print()
            print("Você sabe que essa seria uma batalha perigosa...")
            print("Então fez o correto em fugir...")
            print("Você corre pela sua vida no meio da floresta em rumo a Gruta Drayhill.")
    decisoes4()


def decisoes4():
    print()
    print("Você chega no pé de uma montanha e avista a entrada da Gruta de Drayhill...")
    print("Você vai se aproximando da entrada da gruta, está muito escuro pois a noite já caiu.")
    print("Ao entrar você sente um cheiro estranho, parece ser exofre...")
    print("Está muito escuro dentro da gruta, você só enxerga poucos metros a sua frente...")
    print("Você pega uma tocha da sua mochila...")
    print()
    escolha_str = input("[1] - Não acender a tocha e prosseguir\n"
                        "[2] - Acender a tocha e prosseguir\n"
                        "Escolha: ")
    escolha = int(escolha_str)
    if (escolha == 1):
        print()
        print("Por conta do cheiro de enxofre você acha melhor não acender a tocha.")
        print("Caso aqui tenha gás natural tudo pode explodir...")
        print("Você vai seguindo cuidadosamente o caminho da gruta...")
        print("É um caminho estranho, pois quando mais adentro, mais você vai subindo")
        print("Após andar por uns 20 minutos na completa escuridão...")
        print("Você avista uma luz, parece ser de uma tocha ou lampião...")
        print("Vai se aproximando e encontra uma sala completamente iluminada por tochas.")
        print("Uma silhueta misteriosa reflete na parede...")
        print("Parece ser a sombra de um homem, e parece que ele estava esperando por você...")
        print("Ele percebe sua chegada, com uma voz ecoada ele fala:")
        print("- Então é você o sujeito que quer estragar a diversão dos outros...")
        print("Ele se revela e começa a caminha na sua direção...")
        print("- Achei que você seria mais alto - Ele fala com voz de deboche.")
        print("- Caso você não me conheça, sou Marco Nove Vidas...")
        print("- Sabe o porque tenho esse nome? É que já tentaram me matar 9 vezes...")
        print("- E nenhuma delas conseguiram, então não vai ser você quem vai conseguir...")
        print("- Já que você veio até aqui, saque a sua espada e lute como um homem...")
    elif (escolha == 1):
        print()
        print("Você acende a tocha e seu caminho se ilumina.")
        print("Agora é possível ver algumas escrituras antigas nas paredes.")
        print()
        escolha2_str = input("[1] - Aproximar a tocha e tentar ler as escrituras.\n"
                             "[2] - Ignorar as escrituras e seguir em frente.\n"
                             "Escolha: ")
        escolha2 = int(escolha2_str)
        if (escolha2 == 1):
            print()
            print("As escrituras estão em alguma língua que parece ter sido perdida a muito tempo.")
            print("Mas ao passar a mão sobre elas a tinta sai com facilidade, como se estivesse fresca...")
            print("Isso significa que tem mais alguém nessa caverna...")
            print("Como estão escritas em alguma língua já esquecida você ignora e segue o caminho...")
        elif (escolha2 == 2):
            print()
            print("Você ignora as escrituras pois sua missão é mais importante que isso...")

        print()
        print("Andar pela caverna não é algo tão difícil com uma tocha em mãos")
        print("É um caminho estranho, pois quando mais adentro, mais você vai subindo")
        print("Após uns 10 minutos andando você chega a uma sala completamente iluminada...")
        print("Uma silhueta misteriosa reflete na parede...")
        print("Parece ser a sombra de um homem, e parece que ele estava esperando por você...")
        print("Ele percebe sua chegada, com uma voz ecoada ele fala:")
        print("- Então é você o sujeito que quer estragar a diversão dos outros...")
        print("Ele se revela e começa a caminha na sua direção...")
        print("- Achei que você seria mais alto - Ele fala com voz de deboche.")
        print("- Caso você não me conheça, sou Marco Nove Vidas...")
        print("- Sabe o porque tenho esse nome? É que já tentaram me matar 9 vezes...")
        print("- E nenhuma delas conseguiram, então não vai ser você quem vai conseguir...")
        print("- Já que você veio até aqui, saque a sua espada e lute como um homem...")
        print()
    escolha3_str = input("[1] - Sacar a espada e lutar contra o Marco.\n"
                         "[2] - Convencer o Marco a te deixar passar.\n"
                         "Escolha: ")
    escolha3 = int(escolha3_str)
    if (escolha3 == 1):
        print()
        batalhas.batalha_marco()
    elif (escolha3 == 2):
        print()
        print("Você conversa com o Marco e tenta convencer ele a lhe deixar passar...")
        print("No inicio ele acha bobagem...")
        print("Mas depois ele percebe que oque ele está fazendo é errado e lhe concede passagem...")
    decisoes5()


def decisoes5():
    print()
    print("Após uma longa jornada você sabe que tudo está chegando ao fim...")
    print("Ao sair da gruta você da de cara com a porta de uma torre.")
    print("Este é o Obelisco do Espaço... Uma torre mágica que foi construida no meio de uma montanha...")
    print("As portas parecem ser pesadas demais para se abrir, mas quando você se aproxima elas se abrem sozinhas...")
    print("Uma voz ecoa por toda a torre: ")
    print("- A profecia já dizia que um guerreiro iria aparecer para atrapalhar...")
    print("- Venha guerreiro, siga seu destino...")
    print("Você entra na torra e as portas se fecham atrás de você, é um caminho sem volta...")
    print()
    escolha_str = input("[1] - Subir as escadas da torre com cuidado\n"
                        "[2] - Subir as escadas da torre correndo\n"
                        "Escolha: ")
    escolha = int(escolha_str)

    if (escolha == 1):
        print()
        print("Você vai caminhando em direção as escadas e começa a subir...")
        print("A voz ecoa novamente:")
        print("- Parece que você não está com pressa para salvar o mundo não é mesmo? Hahaha")
        print("Estão lhe provocando mas você ignora e continua a subir lentamente...")
    elif (escolha == 2):
        print()
        print("Você começa a correr em direção das escada, começa a subir...")
        print("Mas quanto mais você corre mais sente que não está saindo do lugar...")
        print("Você olha a sua volta e mal saiu do hall principal da torre...")
        print("A voz ecoa novamente:")
        print("- Hahaha seu tolo, nunca te falaram que a pressa é a inimiga da perfeição? Hahaha...")
        print("Você começa a pensar sobre isso e resolve subir os degraus lentamente...")
        print("Aparentemente isso funciona, mas você sente que é algo que estão usando só para ganhar tempo.")

    print()
    print("A torre é grande e você leva cerca de 15 minutos para subir todos os degraus...")
    print("Ao chegar no topo você observa oque aparente ser um homem de costas para a entrada...")
    print("Ele notou sua presença e fala:")
    print("- Ótimo, como a profecia dizia, seu destino já está selado...")
    print("- Tudo oque preciso fazer agora é matar você e esse velho aqui...")
    print("Você vê o Ilenor preso em uma cela suspensa")
    print("- O mundo dos vivos já passou do seu tempo... Está na hora do mundo dos mortos tomar o controle...")
    print("- Deixa eu me apresentar para você, sou Velazar o Mestre da Escuridão...")
    print("- Mas você pode me chamar de senhor, já que governarei o mundo hahahaha...")
    print("Você sabe que precisa fazer alguma coisa.")
    print("Então você saca sua espada e corre em direção ao necormante")
    print()
    escolha2_str = input("[1] - Atacar Velazar.\n"
                         "[2] - Convencer ele a libartar o mago.\n"
                         "Escolha: ")
    escolha2 = int(escolha2_str)
    if (escolha2 == 1):
        print()
        batalhas.batalha_velazar()
    elif (escolha2 == 2):
        print()
        print("Você tenta conversar com Velazar mas é inútil...")
        print("- Seu tolo, acha mesmo que eu me renderia a você? Um mero mortal? Hahaha...")
        print()
        batalhas.batalha_velazar()
    decisoes6()


def decisoes6():
    print()
    print("A batalha com Velazar foi longa e cansativa, mas tudo está tranquilo agora.")
    print("O mago fala com você:")
    print("- Rápido meu jovem, me tire daqui para podermos sair desse lugar maldito.")
    print("Você ajuda Ilenor a sair da cela...")
    print("Ele agradeçe com a cabeça e fala...")
    print("- Irei abrir um portal para a cidade, vamos logo...")
    print()
    escolha_str = input("[1] - Falar que irá voltar andando até a cidade\n"
                        "[2] - Usar o portal que o Ilenor abriu\n"
                        "Escolha: ")
    escolha = int(escolha_str)
    if (escolha == 1):
        print()
        print("Você fala que prefere voltar caminhando até a cidade...")
        print("O mago parece não se importar com sua decisão e fala:")
        print("- Tudo bem, nos encontramos na cidade...")
        print("Ele entra no portal e some bem na sua frente.")
        print("Você começa a descer as escadas, passa pela caverna...")
        print("Na volta você prefere ir pela estrada principal por ser mais segura...")
        print("Se encontra com uma caravana de comerciantes e segue com eles até a capital...")
        print("Quando chega na portão da cidade um guarda avista você e grita:")
        print("- Rápido, abram os portões, o garoto retornou com vida...")
        print("- Chamem a Princesa Andromeda...")
        print()
        print("Você vai caminhando até a praça da cidade...")
        print("Uma multidão alegre está cercando você, eles gritam e batem palmas para você...")
        print("A Princesa está te esperando em cima de um palanque com uma multidão em volta.")
        print("Você sobe e a princesa comaça a falar:")
        print("- Hoje estamos aqui com um herói, um homem que provou ser leal e bom para seu reino...")
        print("- Pelo seu feito eu irei lhe declarar agora um homem nobre...")
        print("- Eu o declaro O Campeão da Capital")
        print("A população aplaude e grita com muita alegria...")
        print("Todos estão a salvo graças a você...")

    elif (escolha == 2):
        print()
        print("Ilenor abre o portal bem na sua frente...")
        print("Ele fala:")
        print("- Vamos garoto, esse portal nos levará para a entrada da cidade...")
        print("Você e ele entram no portal")
        print("Você se sente estranho mas essa sensação passa rapidamente...")
        print("Quando você menos espera está parado em frente aos portões da cidade...")
        print("Um guarda avista você e Ilenor e grita:")
        print("- Rápido, abram os portões, o garoto retornou com o Ilenor...")
        print("- Chamem a Princesa Andromeda...")
        print()
        print("Você e Ilenor vão caminhando até a praça da cidade...")
        print("Uma multidão alegre está cercando você, eles gritam e batem palmas para você...")
        print("A Princesa está te esperando em cima de um palanque com uma multidão em volta.")
        print("Você sobe e a princesa comaça a falar:")
        print("- Hoje estamos aqui com um herói, um homem que provou ser leal e bom para seu reino...")
        print("- Pelo seu feito eu irei lhe declarar agora um homem nobre...")
        print("- Eu o declaro O Campeão da Capital")
        print("A população aplaude e grita com muita alegria...")
        print("Todos estão a salvo graças a você...")
    reiniciar()


def reiniciar():
    print()
    print("Fim de Jogo, deseja reiniciar o jogo?")
    escolha_str = input("[1] - Reinicar Jogo.\n"
                        "[2] - Sair.\n"
                        "Escolha: ")
    escolha_fim = int(escolha_str)
    if (escolha_fim == 1):
        print()
        print()
        print()
        iniciar_jogo()
    elif (escolha_fim == 2):
        print()
        print("Fim de jogo :)")
        sys.exit()


if (__name__ == "__main__"):
    iniciar_jogo()
