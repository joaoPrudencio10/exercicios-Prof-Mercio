deslocamento = int(input("Digite o deslocamento: "))  # Solicita ao usuário que digite o valor do deslocamento e o converte para um número inteiro.

texto = input("Digite o texto a ser criptografado: ")  # Solicita ao usuário que digite o texto a ser criptografado e armazena na variável 'texto'.

texto_criptografado = ""  # Inicializa uma variável vazia para armazenar o texto criptografado.

for letra in texto:  # Inicia um loop que percorre cada caractere do texto fornecido pelo usuário.

    if letra.isupper():  # Verifica se o caractere atual é uma letra maiúscula.

        letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)  # Converte a letra maiúscula para minúscula, aplica o deslocamento, ajusta para a faixa do alfabeto e a converte de volta para maiúscula.

    elif letra.islower():  # Verifica se o caractere atual é uma letra minúscula.

        letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97)  # Aplica o deslocamento à letra minúscula, ajusta para a faixa do alfabeto e a converte de volta para minúscula.

    else:  # Se o caractere não for uma letra (pode ser um espaço ou pontuação).

        letra_criptografada = letra  # Mantém o caractere não alfabético inalterado.

    texto_criptografado += letra_criptografada  # Adiciona o caractere criptografado (ou não alterado) à variável 'texto_criptografado'.

print("Texto criptografado:", texto_criptografado)  # Exibe o texto criptografado final ao usuário.
