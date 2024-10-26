class MinHeapsArray():
    
    def __init__(self) -> None:
        self.heap = []
        self.size = 0
          
    def swap(self, indx_1, indx_2):
        temp = self.heap[indx_1]
        self.heap[indx_1] = self.heap[indx_2]
        self.heap[indx_2] = temp

    def peek_min(self):
        if not self.size:
            print("Heap is empty")
        else:
            print(self.heap[0])     
        
    def get_min_no(self):
        if not self.size:
            print("Heap is empty")
        else:
            element = self.heap[0]
            # self.heap[0] = self.heap[self.size - 1]
            self.swap(0, self.size - 1)
            self.size -= 1
            self.heapifyDown(0)
            return element
        
    def insert_data(self, data):
        self.size += 1
        self.heap.append(data)
        self.heapifyUp(self.size - 1)
        
    def heapifyDown(self, index):
        left_child = (index * 2) + 1
        right_child = (index * 2) + 2
        
        if left_child < self.size and self.heap[left_child] < self.heap[index]:
            self.swap(left_child, index)
            self.heapifyDown(left_child)
            
        if right_child < self.size and self.heap[right_child] < self.heap[index]:
            self.swap(right_child, index)
            self.heapifyDown(right_child) 
        
    def heapifyUp(self, index):
        parent_indx = index // 2
        print('parent indx', parent_indx)
        if parent_indx >= 0 and self.heap[index] < self.heap[parent_indx]:
            self.swap(index, parent_indx)
            self.heapifyUp(parent_indx)
            
    def print_elements(self):
        for i in range(self.size):
            print(self.heap[i])
    
    def print_all_elements(self):
        for i in self.heap:
            print(i)
            

hp = MinHeapsArray()

hp.insert_data(3)
hp.insert_data(5)
hp.insert_data(9)
hp.insert_data(2)
hp.insert_data(11)
hp.insert_data(1)
hp.insert_data(6)

print('PRE popping of elements')
hp.print_elements()
hp.get_min_no()
print('POST popping of elements 1')
hp.print_elements()
print('POST popping of elements 2')
hp.get_min_no()
hp.print_elements()
print('POST popping of elements 3')
hp.get_min_no()
hp.print_elements()
print('POST popping of elements 4')
hp.get_min_no()
hp.print_elements()
print('POST popping of elements 4')
hp.get_min_no()
hp.print_elements()
print('POST popping of elements 4')
hp.get_min_no()
hp.print_elements()

print('Printing the elements in the list')
hp.print_all_elements()
        