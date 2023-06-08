from task_tools import Any, collect


class ring:
    """permanent tasks, cannot be remove once added. The iteration will not stop automatically also"""

    def __init__(self) -> None:
        self.contents = {}
        self.length = 0

    def append(self, task: Any) -> int:
        self.contents[self.length] = task
        self.length += 1
        return self.length-1

    def pop(self) -> Any:
        return self.__next__()

    def __iter__(self) -> Any:
        self.cur_index = 0
        return self

    def __next__(self) -> Any:
        if self.cur_index >= self.length:
            self.cur_index = 1
            collect()
            return self.contents[0]
        else:
            self.cur_index += 1
            return self.contents[self.cur_index-1]

    def __getitem__(self, key: int) -> Any:
        if key > self.length-1:
            return None
        return self.contents[key]

    def __setitem__(self, key: int, task: Any) -> None:
        self.contents[key] = task

    def __len__(self) -> int:
        return self.length

    def is_empty(self) -> bool:
        return self.length == 0


class node:
    def __init__(self, task: Any) -> None:
        self.task = task
        self.next = None


class linked_node_list:
    def __init__(self, root: Any = None) -> None:
        self.root = None
        self.length = 0

    def append(self, task: Any) -> None:
        """add to the tail"""
        if self.root == None:
            self.root = node(task)
            self.length = 1
        else:
            self.root: node
            current_node = self.root
            while current_node.next != None:
                current_node = current_node.next
            current_node.next = node(task)
            self.length += 1

    def push(self, task: Any) -> None:
        """add to the head"""
        if self.root == None:
            self.root = node(task)
            self.length = 1
        else:
            new_root = node(task)
            new_root.next = self.root
            self.root = new_root
            self.length += 1

    def remove(self, task_id: int = -1) -> Any:
        """remove a task node from list, default remove tail is not assigned"""
        # empty list
        if self.length == 0:
            return None

        current_node = self.root
        # remove tail
        if task_id == -1:
            # last node from tail
            while (current_node.next.next != None):
                current_node = current_node.next
            val_backup = current_node.next.task
            current_node.next = None
            self.length -= 1
            collect()
            return val_backup
        # remove head
        if task_id == 0:
            val_backup = self.root.task
            self.root = self.root.next
            self.length -= 1
            collect()
            return val_backup

        # found at root
        if current_node.task.task_id == task_id:
            # move root to next, save value backup, remove
            self.root = current_node.next
            val_backup = current_node.task
            self.length -= 1
            collect()
            return val_backup
        else:
            # the linked node list only has a root, and not at root
            if current_node.next == None:
                return None

            # if not at root and length is not 1
            while (current_node.next != None):
                if current_node.next.task.task_id == task_id:
                    val_backup = current_node.next.task
                    current_node.next = current_node.next.next
                    self.length -= 1
                    collect()
                    return val_backup
                else:
                    current_node = current_node.next
            collect()
            return None

    def is_empty(self) -> bool:
        return self.length == 0

    def __iter__(self) -> Any:
        self.current_node = self.root
        return self

    def __next__(self) -> Any:
        if self.current_node != None:
            task = self.current_node.task
            self.current_node = self.current_node.next
            return task
        else:
            collect()
            raise StopIteration

    def __len__(self) -> int:
        return self.length


class stack:
    def __init__(self) -> None:
        self.node_list = linked_node_list()

    def append(self, task: Any) -> None:
        self.node_list.push(task)

    def pop(self) -> Any:
        return self.node_list.remove(0)

    def is_empty(self) -> bool:
        return self.node_list.is_empty()


class queue:
    def __init__(self) -> None:
        self.node_list = linked_node_list()

    def append(self, task: Any) -> None:
        self.node_list.append(task)

    def pop(self) -> Any:
        return self.node_list.remove()

    def is_empty(self) -> bool:
        return self.node_list.is_empty()


class task_container:
    def __init__(self) -> None:
        self.results = {}
        # you don't want to see detached thread running forever so no ring
        self.priority_container = {"detached": [stack(), queue()]}
        for i in range(-2, 3):
            self.priority_container[i] = [ring(), stack(), queue()]

    def is_empty(self, priority=0) -> bool:
        return self.priority_container[priority][0].is_empty() and self.priority_container[priority][1].is_empty() and self.priority_container[priority][2].is_empty()

    def __str__(self) -> str:
        return str(self.priority_container)
