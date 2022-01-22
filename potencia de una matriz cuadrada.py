# def potencia(M, n):
#     """Potencia de una matriz"""
#     if n==1:
#         return M
#     else:
#         A=M
#         for i in range(2, n+1):
#             A=producto(M, A)
#         return A

# def det(M):
#     """Resuelve el determinante de la matriz M"""
#     if cuadrada(M):
#         if y(M)==1:
#             return M[0][0]
#         elif y(M)==2:
#             return (M[0][0]*M[0][3])-(M[0][2]*M[0][1])
#         elif y(M)==3:
#             return ((M[0][0]*M[0][4]*M[0][8])+(M[0][2]*M[0][3]*M[0][7])+(M[0][1]*M[0][5]*M[0][6]))-((M[0][2]*M[0][4]*M[0][6])+(M[0][1]*M[0][3]*M[0][8])+(M[0][0]*M[0][5]*M[0][7]))
#         else:
#             f1=fila(M, 1)
#             deter=0
#             for n in range(y(M)):
#                 subM=[]
#                 for nfila in range(2, y(M)+1):
#                     fi=fila(M, nfila)
#                     del fi[n]
#                     subM+=fi
#                 deter+=f1[n]((-1)*n)*det([subM, [y(M)-1, y(M)-1]])
#             return deter

# def traspuesta(M)

 M = [[1,2],[3,4]]
 


def dibujaMatriz(M):
    for i in range(len(M)):
        print '[',
        for j in range(len(M[i])):
            print '{:>3s}'.format(str(M[i][j])),
        print ']'

dibujaMatriz(m)