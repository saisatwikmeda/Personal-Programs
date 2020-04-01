# Sai Satwik Reddy Meda

def countBits(n):
    ans_list = []
    while n > 0:
        if n % 2 ==1:
            ans_list.append(1) 
        n = n // 2
        
    print(ans_list)
    return len(ans_list)
countBits(1234)


def countBits(n):