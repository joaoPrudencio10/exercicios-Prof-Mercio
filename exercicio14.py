numeros = []


for i in range(10):
  
   try:
     numero = int(input("Digite um número inteiro: ")) 
     numeros.append(numero)

   except ValueError: 
    print("Entrada inválida!!!") 
soma = sum(numeros) 
media = soma / len(numeros) 
print("Soma:", soma) 
print("Média:", media)