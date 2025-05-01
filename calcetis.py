#Método que retorna se é possível ter frete grátis ou não
def frete(valor, produtos, precos):
    for i in range(produtos - 2): #For pra percorrer a lista dos preços, produtos-2 pra reduzir o tamanho da lista, já que temos 2 ponteiros.
        inicio = i + 1 #Ponteiro que começa após o índice atual, pra evitar comparar com o mesmo produto
        fim = produtos - 1 #Ponteiro que começa no final da lista
        while inicio < fim: #Enquanto o inicio for menor que o fim, podemos continuar movendo os ponteiros
            soma = precos[i] + precos[inicio] + precos[fim] #Soma do valor atual da variavel que está rodando no for, com o ponteiro inicial e o ponteiro final
            if soma == valor: #Verifica se a soma bate exatamente com o valor necessário
                return ("fretegratis") #Se sim, é possível obter frete grátis. O return sempre encerra o método, então fretegratis é impresso e retornamos para o main.
            elif soma < valor: 
                inicio += 1 #Se a soma dos 3 for menor que o valor que queremos então movemos o ponteiro da esquerda para a direita.
            else:
                fim -= 1 #Se a soma for maior, move o ponteiro da direita para a esquerda.
#O preços.sort() faz a diferença aqui nesse while, pois quando movemos o ponteiro inicio para a direita, sempre pegaremos um valor maior, e quando movemos o ponteiro fim para a esquerda pegamos um valor menor.            
    return ("fretepago") #Se nenhuma combinação for encontrada, retorna que o frete é pago

atual, produtos = map(int, input().split()) #Pega as entradas do preço do carrinho e da quantia de produtos ainda disponiveis.
valor = 200 - atual #Variável que armazena o valor que queremos chegar
precos = [] #Vetor vazio para armazenar o preço dos produtos ainda disponiveis

for i in range(produtos): #For que roda o mesmo número de vezes de produtos ainda disponiveis
    precos.append(int(input()))  #Adiciona o valor de cada produto no vetor precos

precos.sort() #Organiza os preços em ordem crescente

print(frete(valor, produtos, precos))# Chama a função e imprime a string retornada
