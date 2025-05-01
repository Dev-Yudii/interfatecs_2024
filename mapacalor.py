#Estabelecer variáveis
superior = esquerda = centro = direita = inferior = 0

#receber entrada
usuarios = int(input())
for i in range(usuarios):
    entrada = []
    for j in range(6):
        entrada.append(list(map(int, input().split())))
    superior += sum(entrada[0])
    inferior += sum(entrada[5])
    esquerda += sum(i[0] for i in entrada[1:5])
    centro   += sum(i[1] for i in entrada[1:5])
    direita  += sum(i[2] for i in entrada[1:5])

regioes = {
    'superior' : superior,
    'inferior' : inferior,
    'esquerda' : esquerda,
    'centro'   : centro,
    'direita'  : direita
}

print(max(regioes, key=regioes.get))
