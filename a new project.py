#冒泡排序
def bubble_sort(t):
    length = len(t)
    for i in range(length-1):
        for j in range(length-1-i):
            if t[j] > t[j+1]:
                t[j],t[j+1] = t[j+1],t[j]
    return t

#t = [4,5,1,6,2,7,3,8]
#bubble_sort(t)

#输出最小的K个数
while True:
    try:
        lista = [4,5,1,6,2,7,3,8]
        k = int(input())
        la = len(lista)
        listb = []
        if la >= k:
            listc = bubble_sort(lista)
            listb = listc[:k]
        print(listb)
    except:
        break
        
