# autor: Yasmin Hernandes

def binarysearch(alist, item):
    first_item = 0
    last_item = len(alist)-1

    while first_item <= last_item:
        middle = (first_item + last_item)//2
        if alist[middle] == item:
            return middle
        else:
            if item < alist[middle]:
                last_item = middle - 1
            else: 
                first_item = middle + 1
    return 0

alist = [100, 50, 20, 34, 16, 80, 74, 25, 8, 19, 1, 4, 17, 21]
print("O item está no índice: ", binarysearch(alist, 74)) # busca o item 74
print("O item está no índice: ", binarysearch(alist, 20)) # busca o item 20