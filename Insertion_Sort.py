#Sai Meda 
#Insertion Sort Implemention - Pyhton 3.6

L = [6,7,3,1,8,4,2]

def Ins_sort(L):
    k = 0 

    while True:
        if L[k] > L[k+1]:
            L[k],L[k + 1] = L[k + 1], L[k]
            k += 1
            Ins_sort(L)
        else:
            return L
        

print(Ins_sort(L))
