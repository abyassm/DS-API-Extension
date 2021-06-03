class Node:

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:

    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        l = []
        if self.head is None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_ll(self):

        ll_string = ""
        node = self.head

        if node is None:
            print(None)
        while node:

            ll_string += f"{str(node.data)}->"
            node = node.next_node

        ll_string += "None"

        print(ll_string)

        return

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
        # new_node = Node(data, None)
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):

        node = self.head

        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node

        return None

        # l1 = LinkedList()
        # l1.insert_beginning("1")
        # l1.insert_beginning("2")
        # l1.insert_beginning("3")
        # l1.insert_beginning("4")
        # l1.insert_at_end("9")
        # l1.print_ll()
        # print(l1.head.data)
        # print(l1.last_node.data)
