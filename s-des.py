key10 = "1010000010"
p10 = key10[2] + key10[4] + key10[1] + key10[6] + key10[3] + key10[9] + key10[0] + key10[8] + key10[7] + key10[5]

def leftShift(string,x):
    tamanho = len(string)
    return (string[x:] + string[:x])

def p8(string):
    return (string[5] + string[2] + string[6] + string[3] + string[7] + string[4] + string[9] + string[8])

p10shifted = leftShift(p10[:5],1) + leftShift(p10[5:],1)
print(p10shifted)

p8key1 = p8(p10shifted)
print(p8key1)

p10shifted2 = leftShift(p10[:5],3) + leftShift(p10[5:],3)
print(p10shifted2)

p8key2 = p8(p10shifted2)
print(p8key2)