#Sai Satwik Reddy Meda
#Converting a binary array to a number. 
def binary_array_to_number(arr): #Initial thoughts
  final = 0
  arr.reverse()
  s = 0 
  for i in arr:
      final += i * 2 ** s
      s += 1
  return final


def binary_array_to_number2(arr): # A better approach
    s = 0
    for digit in arr:
        s = s * 2 + digit
        print(s)

    return s




