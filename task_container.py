from task_tools import Any, collect
from task_body import task


class ring:
    """permanent tasks, cannot be remove once added. The iteration will not stop automatically also"""

    def __init__(self) -> None:
        self.contents = {}
        self.length = 0

    def append(self, task: task) -> int:
        self.contents[self.length] = task
        self.length += 1
        return self.length-1

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

    def __setitem__(self, key: int, task: task) -> None:
        self.contents[key] = task

    def __len__(self) -> int:
        return self.length


class node:
    def __init__(self, task: task) -> None:
        self.task = task
        self.next = None


class linked_node_list:
    def __init__(self, root: task = None) -> None:
        self.root = None
        self.length = 0

    def append(self, task: task) -> None:
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

    def push(self, task: task) -> None:
        """add to the head"""
        if self.root == None:
            self.root = node(task)
            self.length = 1
        else:
            new_root = node(task)
            new_root.next = self.root
            self.root = new_root
            self.length += 1

    def remove(self, task_id: int = -1) -> None:
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

    def __iter__(self):
        self.current_node = self.root
        return self

    def __next__(self):
        if self.current_node != None:
            task = self.current_node.task
            self.current_node = self.current_node.next
            return task
        else:
            collect()
            raise StopIteration

    def __len__(self):
        return self.length


class stack:
    pass
