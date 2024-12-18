#criação da chave

#permutação 10 elementos
def p10(string):
    return string[2] + string[4] + string[1] + string[6] + string[3] + string[9] + string[0] + string[8] + string[7] + string[5]

#shift logico
def leftShift(string,x):
    tamanho = len(string)
    return (string[x:] + string[:x])

#permutação de 8 elementos
def p8(string):
    return (string[5] + string[2] + string[6] + string[3] + string[7] + string[4] + string[9] + string[8])

#permutação inicial
def InitialPermutation(string):
    return string[1] + string[5] + string[2] + string[0] + string[3] + string[7] + string[4] + string[6]

#permutação final
def ReversePermutation(string):
    return string[3] + string[0] + string[2] + string[4] + string[6] + string[1] + string[7] + string[5]

#pega a parte da esquerda /direita do texto
def getLeft(string):
    return string[:4]
def getRight(string):
    return string[4:]
    
    
#funçao de expansão
def expansion(string):
    return int((string[3] + string[0] + string[1] + string[2] + string[1] + string[2] + string[3] + string[0]),2)

#pega as coordenadas para usar nas tabelas S
def cords(string):
    list = []
    for i in [string[0] + string[3], string[1] + string[2], string[4] + string[7], string[5] + string[6]]:
        list.append(int(i,2))
    return list

#pega os valores da tabela S
def S_table(lista):
    
    s0 = [[1,0,3,2],
          [3,2,1,0],
          [0,2,1,3],
          [3,1,3,2]]

    s1 = [[0,1,2,3],
          [2,0,1,3],
          [3,0,1,0],
          [2,1,0,3]]
    
    y1 = lista[0]
    x1 = lista[1]
    y2 = lista[2]
    x2 = lista[3]
    
    return (s0[y1][x1], s1[y1][x2])

#permutação de quatro elementos
def P4(string):
    return string[1] + string[3] + string[2] + string[0]

#switch dos dois lados
def SW(string):
    return string[4:] + string[:4]

#converte um binario em string do tamanho desejado, adicionando 0 à esquerda e tirando o 0b
def binToString(bin0,size):
    string = str(bin0)[2:]
    while(len(string) < size):
        string = "0" + string
    return string

#calcula as chaves de 8 bits a partir da de 10 bits
def getKeys(key):
    key = p10(key)

    shift1 = leftShift(key[0:5],1)
    shift2 = leftShift(key[5:],1)

    key1 = p8(shift1 + shift2)

    shift1 = leftShift(key[0:5],3)
    shift2 = leftShift(key[5:],3)

    key2 = p8(shift1 + shift2)
    
    return(key1,key2)

#função F do algoritimo
def F(right,key):
    expand = (expansion(right))

    expandXor = binToString(bin(expand ^ int(key,2)),8)

    coordenadas = cords(expandXor)

    tabela = S_table(coordenadas)

    f = binToString(bin(tabela[0]),2) + binToString(bin(tabela[1]),2)
    p4 = P4(f)
    return p4




def encript(key10,inputString):
    key1,key2 = getKeys(key10)
    ip = InitialPermutation(inputString)
    left = getLeft(ip)
    right = getRight(ip)
    
    f = F(right,key1)
    
    p4xorleft = int(f,2) ^ int(left,2)
    left = binToString(bin(p4xorleft),4)
    full = left + right
    full = SW(full)
    
    left = getLeft(full)
    right = getRight(full)
    
    f = F(right,key2)
    
    p4xorleft = int(f,2) ^int(left,2)
    left = binToString(bin(p4xorleft),4)
    
    return ReversePermutation(left + right)

def decript(key10,inputString):
    key1,key2 = getKeys(key10)
    ip = InitialPermutation(inputString)
    left = getLeft(ip)
    right = getRight(ip)
    
    f = F(right,key2)
    
    p4xorleft = int(f,2) ^ int(left,2)
    left = binToString(bin(p4xorleft),4)
    full = left + right
    full = SW(full)
    
    left = getLeft(full)
    right = getRight(full)
    
    f = F(right,key1)
    
    p4xorleft = int(f,2) ^int(left,2)
    left = binToString(bin(p4xorleft),4)
    
    return ReversePermutation(left + right)

#print(encript("1010000010","11010111"))
#print(decript("1010000010","10101000"))

      
modo = input("digite 0 para encriptar ou 1 para decifrar \n")
chave = input("digite uma chave binaria 10 bits \n")
entrada = input("digite uma entrada binaria 8 bits \n")

if(modo == "0"):
    print(encript(chave,entrada))
elif(modo == "1"):
    print(decript(chave,entrada))
    

input("digite qualquer coisa para fechar o programa")