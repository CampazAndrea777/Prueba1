def numPrimos(numInicial,numFinal):
    listaNumerosPrimos = []

    if numInicial < 2:
        numInicial = 2
        
    if (numInicial<= numFinal):
        for entero in range(numInicial, numFinal + 1):
            for i in range(2, entero):
                if entero % i == 0:
                    break
            else:
                 listaNumerosPrimos.append(entero)
    return listaNumerosPrimos    
print (numPrimos(1,100))