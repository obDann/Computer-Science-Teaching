class Node():

    def __init__(self, data):
        '''
        (Node, Object) -> None

        Instantiate a node
        '''
        self.data = data
        self.pointer = None

    def __str__(self):
        return str(self.data)

class LinkedList():

    def __init__(self):
        self.head = None

    def prepend(self, data):
        '''
        (LinkedList, int) -> None

        Add an object to the front of the list
        '''
        if self.head is None:
            some_var = Node(data)
            self.head = some_var
        else:
            another_node = Node(data)
            another_node.pointer = self.head
            self.head = another_node

    def append(self, data):
        '''
        (LinkedList, int) -> None

        Add an object to the end of the list
        '''
        if self.head is None:
            var_1 = Node(data)
            self.head = var_1
        else:
            var_2 = Node(data)
            traveller = self.head
            while traveller.pointer is not None:
                traveller = traveller.point
            traveller.pointer = var_2
            self.head = traveller.pointer