class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        """head is sentinel node, alwasys in position 0.
        """
        self.head = None

    def isEmpty(self):
        return self.head is None

    def gen_list(self):
        """
        generator of linked list
        """
        node = self.head
        while node is not None:
            this_node = node
            node = node.next
            yield this_node
        yield node

    def toList(self) -> list:
        """
        convert linked list to list
        """
        g = self.gen_list()
        mylist = []
        while True:
            node = next(g)
            if node is None:
                break
            else:
                #print(node.data)
                mylist.append(node.data)
        return mylist

    def addNode(self, data):
        """
        put node on the first place
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            old_first = self.head
            self.head = new_node
            new_node.next = old_first


    def appendNode(self, data):
        """
        append node to the end of the list
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            the_next = self.head
            while True:
                if the_next.next is None:
                    the_next.next = new_node
                    break
                else:
                    the_next = the_next.next


    def insertNode(self, index, data) -> bool:
        """
        insert node to the end of the list
        """
        new_node = Node(data)

        if index == 0:
            if self.head is not None:
                new_node.next = self.head
            self.head = new_node
            return True

        if index > 0 and self.head is not None:
            #iterator
            g = self.gen_list()
            this_node = None
            for i in range(index):
                this_node = next(g)
                if this_node is None:
                    return False
            else:
                this_node.next = new_node
            next_node = next(g)
            new_node.next = next_node
            #print(next_data)
            return True
        return False


    def getLength(self) -> int:
        """
        return number of nodes
        """
        g = self.gen_list()
        len = 0
        while True:
            node = next(g)
            if node is not None:
                len += 1
            else:
                break
        return len


    def getNode(self, index: int):
        if index < 0:
            return None
        #iterator
        i = 0
        g = self.gen_list()
        while True:
            node = next(g)
            if node is None: return None
            if i==index: return node
            i += 1
        return None
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return [3]
            