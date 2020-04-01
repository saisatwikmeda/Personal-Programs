#Sai Satwik Reddy Meda
# Returning the length of the smallest word in a given string
def find_short(s):
    L = s.split(' ') #split list
    final = ""
    final = L[0] 
    for i in range(len(L)):
        if len(final) > len(L[i]):
            final = L[i] # Assign smallest word everytime it changes
        i += 1
    return len(final) # returning length of hte smallest word


#Alternatively

def find_short(s):
    return min(len(x) for x in s.split())
#After learning more python 