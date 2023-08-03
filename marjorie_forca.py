'''
Marjorie Aparecida Cortez Daenecke
Jogo da Forca
BCC 1 
'''
import random #importando a biblioteca pra gerar uma palavra aleatoria
import string
from colorama import Fore, Style, Back #para fins esteticos (mudar a cor das palavras)


# Essa função recebe uma lista de palavras como entrada e retorna uma palavra aleatória dessa lista.
def sortear_palavra():
    palavra_sorteada = ''
    with open("./forca.txt") as arquivo: #aqui abriremos um arquivo repleto de palavras
        palavras = arquivo.readlines()
        palavra_sorteada = random.choice(palavras) #sorteando uma aleatoria
    return palavra_sorteada

# Essa função define o número de chances de acordo com a dificuldade escolhida pelo usuário         
def dificuldade(dif):  

    if dif == ("normal"):  # caso o usuario escolha normal ele tera 6 chances
        chances = 6
        start = "Está preparado? Vamos nessa!" #mensagem que aparece de acordo com a dificuldade que o úsuario escolheu
    elif dif == "tormento":
        chances = 4
        start = "Vamos nessa!"
    elif dif == "inferno":
        chances = 2
        start = "Parece que você gosta de um bom desafio, não é mesmo?!"
    elif dif == "nightmare":
        chances = 1
        start = "Boa sorte, vai precisar!"
    else: #caso o usuario digite qualquer coisa diferente das opições o programa ira reestarta
        print("")
        print("Essa dificuldade não está disponivel")
        print("")
        print("Digite uma dificuldade valida, use letras minusculas") #orientação ao usuario
        main()
    # mostra no terminal o numero de chances e a msg quando a função é chamada
    return chances, start

#Pergunta se o jogador quer joga novamente
def jogar_dnv():
    
    nome =""
    jogar_dnv = input("Você quer jogar novamente? Digite -s- para sim, ou -n- para não: ") #pergunta se o jogador quer jogar novamente
    if jogar_dnv == "s": #caso o jogador responde s (sim), ele chamara a main() e vai restarta o programa
        print("")
        print("Assim que é bom! Vamos lá!")
        main ()
        print()
    elif jogar_dnv == "n": #caso ele não queira, o programa acaba
        print("Adeus! Obrigada por jogar, mais sorte na proxima :)")
    else: #qualquer resposta diferente de s (sim) ou n (não), ele tem que responder novamente
        print("Coloque s ou n!")


def tracinhos(palavras_sorteada):  # a cada letra na palavra sorteada ele vai por um traço 
    teste=''
    for i in palavras_sorteada: #esse comando pricipal da criação destes traços
        teste +='_'
    return teste


def desenho(chances,dif): #desenhos que irão aparecer toda vez que o jogador digita uma letra
    #chances, dif = dificuldade(dif)
    print(dif,chances)


    if (dif == "normal" and chances == 6) or (dif == "tormento" and chances == 4) or (dif == "inferno" and chances == 2) or (dif == "nightmare" and chances == 1):
        print(Fore.GREEN)
        print("------------------------------------------")
        print("|----------|                              ")
        print("|          |            ☁️    ☁️  🌞☁️  ")
        print("|                                         ")
        print("|                    ☁️     ☁️           ")
        print("|                                 ☁️     ")
        print("|                          /\            ")
        print("|                         //\\           ")
        print("|                        ///\\\          ")
        print("|                       ////\\\\         ")
        print("_|_                    /////\\\\\        ")
        print("|   |______           //////\\\\\\       ")
        print("|          |         ///////\\\\\\\      ")
        print("|          |               |||           ")
        print("---------------------------|||-----------")
        print("🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺")

    elif (dif == "normal" and chances == 5):
        print("----------------------------------------")
        print("|----------|                            ")
        print("|          |        ☁️     ☁️  🌞 ☁️  ")
        print("|          O                           ")
        print("|                      ☁️     ☁️       ")
        print("|                               ☁️     ")
        print("|                        /\            ")
        print("|                       //\\           ")
        print("|                      ///\\\          ")
        print("|                     ////\\\\         ")
        print("_|_                  /////\\\\\        ")
        print("|   |______         //////\\\\\\       ")
        print("|          |       ///////\\\\\\\      ")
        print("|          |            |||           ")
        print("------------------------|||-----------")
        print("🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺")

    elif (dif == "normal" and chances == 4) or (dif == "tormento" and chances == 3):
        print("------------------------------------------------")
        print("|----------|                            ")
        print("|          |      ☁️ ☁️  🌞☁️         ")
        print("|          O                            ")
        print("|          |        ☁️     ☁️          ")
        print("|          |                   ☁️      ")
        print("|                            /\        ")
        print("|                           //\\       ")
        print("|                          ///\\\      ")
        print("|                         ////\\\\     ")
        print("_|_                      /////\\\\\    ")
        print("|   |______             //////\\\\\\   ")
        print("|          |           ///////\\\\\\\  ")
        print("|          |                 |||       ")
        print("-----------------------------|||------")
        print("🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 ")

    elif (dif == "normal" and chances == 3) or (dif == "tormento" and chances == 2) or (dif == "inferno" and chances == 1) or (dif == "nightmare" and chances == 1):
        print("---------------------------------------")
        print("|----------|                           ")
        print("|          |          ☁️   ☁️🌞☁️    ")
        print("|          O                           ")
        print("|          |               ☁️     ☁️   ")
        print("|          |                        ☁️ ")
        print("|           \                /\         ")
        print("|                           //\\        ")
        print("|                          ///\\\       ")
        print("|                         ////\\\\      ")
        print("_|_                      /////\\\\\     ")
        print("|   |______             //////\\\\\\    ")
        print("|          |            ///////\\\\\\   ")
        print("|          |                 |||        ")
        print("-----------------------------|||---------")
        print("🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺")

    elif (dif == "normal" and chances == 2) or (dif == "tormento" and chances == 1):
        print("----------------------------------------")
        print("|----------|                            ")
        print("|          |       ☁️  ☁️  🌞  ☁️     ")
        print("|          O                            ")
        print("|          |               ☁️     ☁️    ")
        print("|          |                ☁️          ")
        print("|         / \             /\            ")
        print("|                        //\\           ")
        print("|                       ///\\\          ")
        print("|                      ////\\\\         ")
        print("_|_                   /////\\\\\        ")
        print("|   |______          //////\\\\\\       ")
        print("|          |        ///////\\\\\\\      ")
        print("|          |             |||           ")
        print("-------------------------|||-----------")
        print("🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺")

    elif (dif == "normal" and chances >= 1) or (dif == "tomento" and chances >= 1):
        print("----------------------------------------")
        print("|----------|                           ")
        print("|          |       ☁️        ☁️🌞☁️   ")
        print("|          O                            ")
        print("|          |\          ☁️     ☁️       ")
        print("|          |                    ☁️     ")
        print("|         / \            /\            ")
        print("|                       //\\           ")
        print("|                      ///\\\          ")
        print("|                     ////\\\\         ")
        print("_|_                  /////\\\\\        ")
        print("|   |______         //////\\\\\\       ")
        print("|          |       ///////\\\\\\\      ")
        print("|          |             |||           ")
        print("-------------------------|||-----------")
        print("🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺  🌺 🌺 🌺")


def main():  # Esse é o caminho principal
    
    letras_erradas = [] #lista vazia que irá constantemente ser preenchida com as letras escolhidas pelo usuario
    letras_certas =  []
    letras_escolhidas = [letras_erradas + letras_certas] 

    print("") # estetica  
    print(Fore.YELLOW + Style.BRIGHT)  
    print("------------------------------------------------")
    print(" |⭐ SEJA BEM-VINDO AO TENEBROSO JOGO DA FORCA ⭐| ") #introdução ao jogo
    print("\n------------------------------------------------\n \n \n") #esse \n é para quebrar a linha
    print(Fore.RED + Style.DIM) 
    regras = input("Você sabe jogar? Se sim digite s, se não digite n! Se você escolher não, eu te ensino! ")
    print("")
    print(Fore.CYAN)
    if regras == "n": #ensinando a jogar o jogo da forca
        print("\n Como jogar?\n 1. Você recebera uma quantia de traços na tela \n Por exemplo: \n \n"\
        "_ _ _ _ _  \n \n Cada traço é uma letra, a qual você tem que descobrir \n \n"\
        "Mas lembre-se, você chuta uma letra de cada vez, e de acordo com a dificuldade \n"\
        "que você escolher, você terá um número limitado de erros \n \n \n"\
        "2. Escolher uma letra \n \n Vamos supor que você escolheu a letra A \n"\
        "Se a palavra tiver a letra A, o traço será substituido pela letra no lugar que a mesma pertence \n \n \n"\
        "Seguindo o mesmo exemplo \n \n Letra escolhida: A \n \n _ A _ _ _ \n \n"\
        "Agora sabemos que a palavra tem um A, e assim vai, até você descobrir a palavra \n \n"\
        "Contudo, cada vez que você erra uma letra, é denhado em uma forca partes \n \n"\
        "do corpo humano de um homem, o qual, quando fica com todos os membros do corpo \n \n"\
        "significa que foi enforcado, dando fim ao jogo. Game over, derrota. \n")

    elif regras == "s":
        print("Ok")

    else:
        print("Digite s ou n")
        main() #Volta no começo

    print(Fore.BLUE)
    nome = input("Para começar, qual é seu nome? ") #guarda o nome do jogador
    print("") # estetica
    print("Certo,", nome, ", let´s go") 
    print("") # estetica

    palavra_sorteada = sortear_palavra() # chamando a def sortear_palavra para pegar uma palavra aleatoria da lista

    print(Fore.GREEN)
    dif = input("Escolha uma dificuldade! Normal, Tormento, Inferno, Nightmare ") #deixa o usuário escolher a dificuldade
    # chamamos a def dif para mostrar as infos
    chances, start = dificuldade(dif)

    print("")
    # apresentação do numero de chances pro usuario

    print("Você escolheu", dif, "! Você tem,",
          chances, "chances na dificuldade", dif)
    print("") # estetica
    print(start)  # esse start ta dentro da def dificulde
    print("")  # estetica
    
    print(Fore.LIGHTWHITE_EX + Back.BLACK)
    tracos = "_"*(len(palavra_sorteada)-1) 
    print(*tracos)  # imprimir os traços da palavras


    while chances >0: #enquanto o jogador ainda tiver chances
        desenho(chances,dif)
        letra = input("Escolha uma letra: ".lower())[0] #limita o usuario, pegando apenas a primeira letra digitada e a deixa minuscula
        letras_escolhidas = letras_certas + letras_erradas
                            

        if letra in palavra_sorteada: #verifica se a letra que o jogador escolheu está na palavra secreta
            senha=""
            letras_certas.append(letra) #coloca as letras certas na lista letras certas
            if letra in letras_escolhidas: #avisa caso o usuario repita uma letra e não o penalisa por isso
                print("Você já escolheu essa letra!")

            for i in range(len(palavra_sorteada)-1):  #fazendo a substituição de traços por letras

                if palavra_sorteada[i] == letra:
                    senha += letra

                else:
                    senha += tracos[i]

            tracos=senha
            print(*tracos)

            if '_' not in tracos: #verifica se o jogador acertou todas as letras da palavra secreta
                print("ENCONTAMOS UM DEUS GAMER! PARABÉNS VOCÊ VENCEU! A PALAVRA ERA: ", palavra_sorteada, "!")
                jogar_dnv()
                break

        else: #quando a pessoa erra uma letra ela vem por esse caminho
            
            if letra in letras_escolhidas: #verifica se tem letra repitida
                print("Letras errada:", letras_erradas)
                print("Você já escolheu essa letra!")

            else:
                chances -=1 #perde uma chance a cada vez que erra
                print("Você errou!")
                #guardar erros
                letras_erradas.append(letra) #lista com as letras errada que a pessoa digitou
                print("Letras erradas:", ','.join(letras_erradas)) #mostra na tela os erros 
                print(*tracos)
                if chances < 1: #quando não tem mais chances esse é a finalização do jogo
                    print(Fore.RED) #uma cor chamativa pra mostrar que a pessoa perdeu
                    print("----------------------------------------")
                    print("|----------|                           ")
                    print("|          |       ☁️        ☁️🌞☁️   ")
                    print("|          O                            ")
                    print("|         /|\          ☁️     ☁️       ")
                    print("|          |                    ☁️     ")
                    print("|         / \            /\            ")
                    print("|                       //\\           ")
                    print("|                      ///\\\          ")
                    print("|                     ////\\\\         ")
                    print("_|_                  /////\\\\\        ")
                    print("|   |______         //////\\\\\\       ")
                    print("|          |       ///////\\\\\\\      ")
                    print("|          |             |||           ")
                    print("-------------------------|||-----------")
                    print("🌺 🌺 🌺 🌺 🌺 🌺 🌺 🌺  🌺 🌺 🌺")
                    print("Você perdeu! A palavra correta era", palavra_sorteada)
                    print("")
                    #perguntando se a pessoa quer jogar novamente
                    jogar_dnv()
                    print()


        print()
             
            
main()
