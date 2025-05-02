num = int(input()) #Pega o número que iremos checar
count = 0 #Contador de divisores
for i in range(1, num+1): #For que percorre de 1 até o número que queremos checar
    if num%i == 0: 
        count += 1 #Se a divisão for igual a 0 adicionamos 1 ao contador de divisores
        if count > 3: 
            break; #Se a contagem de divisores for maior que 3 saimos do for
if count == 3: 
    print('sim') #Print sim se o número tiver exatamente 3 divisores
else:
    print('nao') #Se tiver um número de divisores for diferente de 3 print nao
