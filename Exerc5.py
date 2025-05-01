tamanhoList = int(input("\nGrupos necessarios "))#Tamanho de perfils identificados necessecarios na formacao do grupo

formacaoGrupos = input("\nformacao de cada grupo ")#formacao do grupo base que forma 1 grupo
grupoBase = formacaoGrupos.split()#transformacao em uma lista com base na entrada

qtdRegioes = int(input("\nQuantas regioes "))#Quantidade de regioes que vao agrupar os grupos

for requisito in range(qtdRegioes):#Loop com quantidades de regioes que precisam dos voluntarios, no fim imprime a resposta de quantos grupos foram alocados
    regiaoDisponivel = input("\ngrupo voluntarios ")#entrada do grupo de voluntarios disponiveis
    grupoVoluntarios = regiaoDisponivel.split()#tranforma a entrada numa lista
    
    minimo = 999#valor que demonstra quantos grupos podem ser alocados com base no grupo de voluntarios

    for disponibilidade in range(tamanhoList):#loop for com tamanho da lista
        
        if int(grupoVoluntarios[disponibilidade + 1]) // int(grupoBase[disponibilidade]) < minimo:  #Se a divisao inteira entre a quantidade de volunt dispon e o 
                                                                                                    #minimo para formar um grupo for menor que o valor minimo, muda o valor minimo
            minimo = int(grupoVoluntarios[disponibilidade + 1]) // int(grupoBase[disponibilidade])  #alteracao do valor limite de grupos formados
            resposta = f"{grupoVoluntarios[0]} {minimo}"#guarda o valor de alocacao do grupo de voluntarios mais a identificacao do grupo
    
    print(resposta)#Saida para cada grupo de voluntarios