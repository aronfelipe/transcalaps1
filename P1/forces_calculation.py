import math
import numpy as np

A = 0.02 #Area
L = 2 #Comprimento
P = 50e3 #Qual a carga aplicada na extremidade da barra?"))
E = 200e9 #Qual o modulo de elasticidade?


# Tensao = P/A
# Deform = Tensao/E
# Desloc = Deform*L

matrix_de_rigidez = np.matrix([[1,-1],[-1,1]])
M1 = np.delete(matrix_de_rigidez,1,1)
M1 = np.delete(M1,1,0)
U = P/(((E*A)/L)*M1)

print(U)