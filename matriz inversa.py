matriz =  [[9,5,1],
          [4,5,6],
          [7,8,9]]

def InversaMatriz():
    nuevaMatriz = []
    for i in range(len(matriz[0])):
        cambio = []
        for j in range(len(matriz)):
            cambio.append(matriz[j][i])
        nuevaMatriz.append(cambio )
    
    return nuevaMatriz 
    
    
print (InversaMatriz() )