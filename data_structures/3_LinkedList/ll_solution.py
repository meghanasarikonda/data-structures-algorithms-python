class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def print_ll(self):
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
                break

            count += 1
            itr = itr.next

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception('Invalid Index')

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        if self.head == None:
            raise Exception('Empty Linked List')

        count = 0
        itr = self.head

        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            count += 1
            itr = itr.next
        print(count)

    def remove_by_value(self, data):
        if self.head == None:
            return

        count = 0
        itr = self.head

        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
            count += 1
            itr = itr.next
        print('value not present in this Linked List')


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at_end(4)
    ll.insert_at_end(5)
    ll.print_ll()
    # print(ll.get_length())
    ll.remove_at(4)
    ll.print_ll()
    # print(ll.get_length())
    ll.insert_at(2, 5)
    ll.print_ll()
    ll.remove_by_value('o')
    ll.print_ll()
    ll.insert_after_value('mango', 'cherry')
    ll.print_ll()
