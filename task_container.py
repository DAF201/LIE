# unfinish, lunch period is over
from typing import Any

from GitHub.TASK.tasks_container import node


class node:

    def __init__(self, data: Any = None) -> None:
        self.__data: Any
        self.last: node
        self.next: node

        self.__data = data
        self.last = None
        self.next = None

    def get(self) -> Any:
        return self.__data

    def replace(self, data) -> None:
        self.__data = data

    def pop(self) -> None:
        self.__data = None

    def __del__(self) -> None:
        pass


# linear linked node list
class linked_node_list:
    def __init__(self, root: node = None) -> None:
        self.root = root

    def append(self, node: node, index: int = -1) -> None:
        pass

    def pop() -> Any:
        pass

    # for iteration?
    def __iter__(): pass
    def __next__(): pass

    # when remove
    def __del__(): pass


# linked node list as a ring keep rotating to get the next task from a fixed position
class ring:
    def __init__(self, current: node = None) -> None:
        self.current = current

    def append(self, new_node: node) -> None:
        last = self.current.last
        last.next = new_node
        new_node.last = last
        new_node.next = self.current
        self.current.last = new_node

    def pop() -> Any: pass

    # for iteration?
    def __iter__(): pass
    def __next__(): pass

    # when remove
    def __del__(): pass


class stack(linked_node_list):
    def __init__(self, root: node = None) -> None:
        super().__init__(root)

    def append(self, node: node) -> None:
        return super().append(node, 0)


class queue(linked_node_list):
    def __init__(self, root: node = None) -> None:
        super().__init__(root)

    def append(self, node: node) -> None:
        return super().append(node, -1)


class task_container(stack, queue, ring):
    def __init__(self, root=None, current=None) -> None:
        stack.__init__(self, root)
        queue.__init__(self, root)
        ring.__init__(self, current)
