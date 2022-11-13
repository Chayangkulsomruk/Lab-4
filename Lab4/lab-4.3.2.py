class Node:
    def __init__(Header, data):
        Header.data = data
        Header.next = None
    def __repr__(Header):
        return Header.data
class LinkedList:
    def __init__(Header):
        Header.head = None
    def __repr__(Header):
        node = Header.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def add_first(Header, node):
        node.next = Header.head
        Header.head = node
    def printLL(Header):
        current = Header.head
        while(current):
            print(current.data)
            current = current.next
AiiL = LinkedList()
I_node = Node(44)
AiiL.head = I_node
II_node = Node(36)
III_node = Node(90)
IV_node = Node(10)
V_node = Node(60)
VI_node = Node(99)
I_node.next = II_node
II_node.next = III_node
III_node.next = IV_node
IV_node.next = V_node
V_node.next = VI_node
AiiL.add_first(Node(104))
AiiL.printLL()

