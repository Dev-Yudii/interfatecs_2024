#O problema pede para que dados 3 números, escolhamos o que não seja o maior nem o menor dos 3.
numeros = list(map(int, input().split())) #Cria uma lista que recebe os 3 inteiros
numeros.sort() #Ordena a lista

print(numeros[1]) #Mostra o segundo valor da lista.
