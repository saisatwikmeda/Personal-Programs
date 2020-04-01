class Node:
    def __init__(self,value, next_node):
        self.value = value 
        self.next_node = next_node
    def __str__(self):
        s = "current value is {}, next value is {}".format(self.value,self.next_node)
        return s

    
head = Node(2,None)
head = Node(1,head)

print(head)



def reverse_list(head):
    new_head = None
    while head:
        head.next_node, head, new_head = new_head, head.next_node, head # look Ma, no temp vars!
    return new_head

print(reverse_list(head))
print((head))