# autor: Yasmin Hernandes

def buscalinear(alist, x):
    for i in range(len(alist)):
        if alist[i] == x:
            return i
    return -1

alist = [100, 50, 20, 34, 16, 80, 74, 25, 8, 19, 1, 4, 17, 21]
print("O item está no índice: ", buscalinear(alist, 16)) # busca pelo item 16
print("O item está no índice: ", buscalinear(alist, 8)) # busca pelo item 8
print("O item está no índice: ", buscalinear(alist, 21)) # busca pelo item 21