from priority import priority


class arr:
    def __init__(self, size) -> None:
        self.__cur_index = size
        self.__arr = [0]*size

    def __len__(self):
        return self.__cur_index

    def __setitem__(self, index, value):
        self.__arr[index] = value

    def __getitem__(self, index):
        return self.__arr[index]

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < self.__cur_index:
            data = self.__arr[self.index]
            self.index += 1
            return data
        else:
            raise StopIteration

    def __str__(self):
        return str(self.__arr)


class heap:
    '''max heap, default capacity: 32, default max: 1073741822'''

    def __init__(self, __size__=33, __zero__=1073741823):
        self.__arr = arr(__size__+1)
        self.__arr[0] = __zero__
        self.__cur_index = 0

    def insert(self, data):
        '''insert a piece of data to heap, return true when success, false when fail(likely because of heap is full)'''
        if self.__cur_index == len(self.__arr)-2:
            return False
        try:
            self.__arr[self.__cur_index+1] = data
            cur_index = self.__cur_index+1
            par_index = cur_index//2

            while (self.__arr[par_index] < self.__arr[cur_index]):
                self.__arr[par_index], self.__arr[cur_index] = self.__arr[cur_index], self.__arr[par_index]
                cur_index = par_index
                par_index = cur_index//2

            self.__cur_index += 1
            return True

        except:
            return False

    def pop(self):
        '''pop the root of the heap, return None when heap is empty'''
        if self.__cur_index == 0:
            return priority()

        data = self.__arr[1]
        self.__arr[1] = 0

        cur_node = 1
        left_child = 2
        right_child = 3

        try:
            while cur_node < self.__cur_index and self.__arr[cur_node] < max(self.__arr[left_child], self.__arr[right_child]):
                if self.__arr[left_child] >= self.__arr[right_child]:
                    self.__arr[cur_node], self.__arr[left_child] = self.__arr[left_child], self.__arr[cur_node]
                    cur_node = left_child
                else:
                    self.__arr[cur_node], self.__arr[right_child] = self.__arr[right_child], self.__arr[cur_node]
                    cur_node = right_child

                left_child = cur_node*2
                right_child = left_child+1
        except:
            # may reach end of array but there is no right child cause the array size issue, but I don't want to limit
            # how to set the size of array
            self.__cur_index -= 1
            return data

        self.__cur_index -= 1
        return data

    def peek(self):
        return self.__arr[1] if self.__cur_index > 0 else None

    def __str__(self):
        return str(self.peek())

    @property
    def __is_empty__(self):
        return self.__cur_index == 0

    @property
    def __zero__(self):
        return self.__arr[0]
