import random

def escolher_palavras():
    palavras = ["apple", "banana", "computer", "happy", "love", "move"]
    return random.choice(palavras)
def exibir_palavra(palavra, letras_corretas):
    exibicao = ""
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra + " "
        else:
            exibicao += "_ "
    return exibicao.strip()

def jogar_forca():
    palavra_secreta = escolher_palavras()
    letras_corretas = []
    letras_erradas = []
    tentativas_maximas = 6
    tentativas = 0

    print("Bem-vindo ao Jogo da Forca!")
    print(exibir_palavra(palavra_secreta, letras_corretas))

    while tentativas < tentativas_maximas:
        letra_escolhida = input("Digite uma letra: ").lower()

        if letra_escolhida.isalpha() and len(letra_escolhida) == 1:
            if letra_escolhida in letras_corretas or letra_escolhida in letras_erradas:
                print("Você já tentou essa letra. Tente novamente.")
            elif letra_escolhida in palavra_secreta:
                letras_corretas.append(letra_escolhida)
                print("Letra correta!")
            else:
                letras_erradas.append(letra_escolhida)
                tentativas += 1
                print(f"Letra incorreta! Tentativas restantes: {tentativas_maximas - tentativas}")

            print(exibir_palavra(palavra_secreta, letras_corretas))
            print(f"Letras erradas: {', '.join(letras_erradas)}")

            if set(letras_corretas) == set(palavra_secreta):
                print("Parabéns! Você ganhou!")
                break
        else:
            print("Por favor, digite uma letra válida.")

    if tentativas == tentativas_maximas:
        print("Você perdeu! A palavra correta era:", palavra_secreta)

    input("Pressione Enter para fechar o jogo.")

if __name__ == "__main__":
    jogar_forca()