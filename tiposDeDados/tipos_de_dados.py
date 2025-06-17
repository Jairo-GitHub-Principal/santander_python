
n1 = int

n2 = float

n3 = str

n1 = 10

n2 = 10.0

n3 = '10'
print(type(n1), "valor",n1)

print(type(n2), "valor",n2)

print(type(n3), "valor",n3)

print (n1 + n2 )

print (True ) # booleano

print (False ) # booleano

var1 = 10
var2 = 10

print (bool(var1 == var2)) # booleano

# para executar esse codigp pelo terminal de o comando python3 tipos_de_dados.py

# converter var1 para string

print ( type(var1), "sera convertido para string:", str(var1),"agora é:",type(str(var1))) # converte var 1 para string

# converter var1 para int

print (type(var1), "que atualmente é string sera convertida para int", int(var1), "agora é:",type(int(var1)) )

print ("\n")
print (" tipos de dados mais usados em python")

'''
Texto        str
Numérico     int, float, complex
Sequência    list, tuple, range
Mapa         dict
Coleção      set, frozenset
Booleano     bool
Binário      bytes, bytearray, memoryview
'''

texto = "jairo"

numerico = 10
numerico2 = 1.5
numerico3 = 3+10j

sequenciaList = [1,2,3,4,5]
sequenciaTuple = (1,2,3,4,5)
sequenciaRange = range(1,10)

colecaoSet = {1,2,3,4,5}

colecaoFrozenSet = frozenset({1,2,3,4,5})


mapa = {    "nome": "jairo",    "idade": 20}

booleano = True

binarioBytes = b'jairo'
binarioByteArray = bytearray(b'jairo')
binarioMemoryView = memoryview(b'jairo')



print(type(texto),texto)
print (type(numerico),numerico)
print (type(numerico2),numerico2)
print (type(numerico3),numerico3)
print (type(sequenciaList),sequenciaList)
print (type(sequenciaTuple),sequenciaTuple)
print (type(sequenciaRange),sequenciaRange)
print (type(mapa),mapa)
print (type(colecaoSet),colecaoSet)
print (type(colecaoFrozenSet),colecaoFrozenSet)
print (type(booleano),booleano)
print (type(binarioBytes),binarioBytes)
print (type(binarioByteArray),binarioByteArray)
print (type(binarioMemoryView),binarioMemoryView)


num = 15 // 2 #divisão com duas / converto o numero pra inteiro
print (type(num),num)
num = 15 / 2 # divisão com // barras converte o numero para float
print (type(num),num) 

num = "10"
print (ParseInt(num))