'''Script que primeiramente recebe um inteiro N sendo que
N está entre 3 e 100. Após isto ele irá mandar 6 linhas,
uma de cada vez, sendo q cada linha possui 3 inteiros separados por 
espaço onde cada inteiro é 1 ou 0, exemplo: 0 0 1 (Isso se repete 6x com cada
                                        valor podendo ser 1 ou 0)
Isso completa 1 conjunto de 6 linhas, depois irá mandar o proximo 
conjunto de 6 linhas.
nesse conjunto de 6 linhas, o trabalho é observar onde está a maior
concentração de 1, na parte superior (linha 1 e 2), no meio (linha 3 e 4)
ou na parte inferior (linha 5 e 6) e entao contar dentre TODOS os conjuntos
recebidos qual foi a regiao mais observada'''

repeticoes = int(input())

contagem = 6                    #contador 2º while
cont = 0                        #contador 1º while
localMaiorRep = [0,0,0]         #contagem de qual linha é a mais usada
regioes = [0,0,0]               #primeiro indice é linha 1 e 2
                                #segundo indice é linha 3 e 4
                                #Tercerio indice é linha 5 e 6


while cont != repeticoes:
    localMaiorRep = [0,0,0]     #contagem de qual linha é a mais usada
    listEntrada = []

    while contagem > 0:         #Entradas das 6 linhas
        entrada = input()
        listEntrada.append(entrada.split(sep = " "))
        contagem = contagem - 1
        
    linha = 0
    localMaiorRep = [0,0,0]     #lista das linhas + usadas
    
    for x in listEntrada:
        soma = 0
        for j in x:
            soma = soma + int(j)

        if linha < 2:
            localMaiorRep[0] += soma
        else:
            if linha < 4:
                localMaiorRep[1] += soma
            else:
                if linha < 6:
                    localMaiorRep[2] += soma

        linha += 1
 
    contagem = 6                #reset da contagem de linha
    cont = cont + 1             #proximo conjunto de numeros
    
    maior = max(localMaiorRep)
    final = localMaiorRep.index(maior)
    regioes[final] += 1

print(localMaiorRep)
print(regioes)

maior = max(regioes)
final = regioes.index(maior)

if final == 2:
    print("inferior")
else:
    if final == 1:
        print("meio")
    else:
        if final == 0:
            print("superior")