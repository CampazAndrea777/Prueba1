def numPrimos(numInicial,numFinal):
    listaNumerosPrimos = []

    if numInicial < 2:
        numInicial = 2
        
    if (numInicial<= numFinal):
        for x in range(numInicial, numFinal):
            for i in range(2, x):
                if x % i == 0:
                    break
            else:
                 listaNumerosPrimos.append(x)
    return listaNumerosPrimos    
print (numPrimos(1,100))