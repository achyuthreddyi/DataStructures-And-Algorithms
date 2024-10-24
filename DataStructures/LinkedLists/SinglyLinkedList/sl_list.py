class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
   
        
class SinglyLinkedList():
    def __init__(self, data) -> None:
        self.head = Node(data)
    
    def add_data_at_end(self, data) -> None:
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)
    
    def add_data_at_start(self, data) -> None:
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node   
        
    def check_if_data_is_present(self, data) -> None:
        current_node = self.head
        
        while current_node:
            if current_node.data == data:
                print("%s data is present in the list" % data)
                return
            current_node = current_node.next
        print("%s data is not present in the given list" % data)
        
    def delete_all_data_in_list(self, data) -> None:
        
        if self.head and self.head.data == data:
            self.head = self.head.next
            return

        if not self.head:
            return
        
        current_node = self.head
        
        while current_node and current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
    
    def delete_first_occ_data_in_list(self, data)-> None:
        if self.head and self.head.data == data:
            self.head = self.head.next
        
        if not self.head:
            return
        
        current_node = self.head
        
        while current_node and current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            
    def delete_first_node(self):
        if self.head:
            print("Deleted first element", self.head.data)
            self.head = self.head.next
            return
        print("No nodes to delete")
        
    def delete_last_node(self):
        if not self.head:
            print("No nodes to delete")
            return
        
        left_node = self.head
        right_node = self.head.next
        
        while right_node.next:
            left_node = right_node
            right_node = right_node.next
        
        left_node.next = None
        
    def count_nodes(self):
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        print('Total elements in the sll ', count)
        
    def print_all_data(self) -> None:
        node = self.head
        
        while node:
            print(node.data)
            node = node.next
            
    def reverse_linked_list(self) -> None:
        if not self.head:
            print("Nothing to reverse")
            return
        
        Left_node = None
        current = self.head
    
        while current:
            right_node = current.next
            current.next = Left_node
            Left_node = current
            current = right_node
            
        self.head = Left_node
        
    def rotate_right_k_times(self, k):
        #  For K times 
        # I will remove last element in the list and append it at the starting
        if not self.head or not self.head.next or k == 0:
            return
        
        length = 1
        last = self.head
        while last.next:
            last = last.next
            length += 1

        # Adjust k if it's larger than the length of the list
        k = k % length
        if k == 0:
            return
        print('k in here is ', k)
        # Find the new last node (length - k - 1 steps from the head)
        new_last = self.head
        for _ in range(length - k - 1):
            new_last = new_last.next

        print(self.head.data)
        print(new_last.data)
        print(last.data)
        # Rotate the list
        
        new_head = new_last.next
        new_last.next = None
        last.next = self.head
        self.head = new_head
       

sll = SinglyLinkedList(1)
# sll.add_data_at_end(1)
# sll.add_data_at_end(5)
# sll.add_data_at_end(6)
# sll.add_data_at_start(7)
# sll.add_data_at_end(9)
# sll.add_data_at_end(9)
# sll.add_data_at_end(9)
# sll.add_data_at_end(1)
# sll.add_data_at_end(2)
sll.add_data_at_end(1)
sll.add_data_at_end(2)
sll.add_data_at_end(3)
sll.add_data_at_end(4)
sll.add_data_at_end(5)
sll.print_all_data()
sll.count_nodes()

sll.rotate_right_k_times(3)
sll.print_all_data()

# sll.reverse_linked_list()
# sll.print_all_data()
# sll.delete_all_data_in_list(1)
# sll.delete_first_occ_data_in_list(9)
# sll.delete_first_occ_data_in_list(2)
# sll.add_data_at_end(2)
# sll.delete_first_node()


# sll.print_all_data()
# sll.delete_last_node()
# print("After deleting")
# sll.print_all_data()
# sll.count_nodes()
