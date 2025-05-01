#Método que retorna o número equivalente a cada uma das letras se ela se encontrar no bloco de strings.
def conversor(letra):
    if letra in "ABC":
        return '2'
    if letra in "DEF":
        return '3'
    if letra in "GHI":
        return '4'
    if letra in "JKL":
        return '5'
    if letra in "MNO":
        return '6'
    if letra in "PQRS":
        return '7'
    if letra in "TUV":
        return '8'
    if letra in "WXYZ":
        return '9'

n = int(input()) #Pega o número de entradas

for i in range(n): #For que roda o mesmo número de entradas
    palavra = input() #Pega cada uma das entradas
    saida = '' #Cria uma string vazia
    for letra in palavra: #For que percorre cada letra da minha entrada atual
        saida += conversor(str(letra)) #Adiciona a entrada na string saida, de acordo com os ifs do método
        
    print(saida)
