# still unfinished, HW is not done yet
from task_tools import Any, collect


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


# linear linked node list (interface like thing)
class linked_node_list:
    def __init__(self, root: node = None) -> None: self.root = root
    def append(self, node: node, index: int = -1) -> None: pass
    def pop(self) -> Any: pass
    # for iteration?
    def __iter__(self) -> Any: pass
    def __next__(self) -> Any: pass
    # when remove
    def __del__(self) -> None: collect()
    # when try to access
    def __enter__(self) -> Any: pass
    def __exit__(self, type, value, trace) -> Any: pass


# linked node list as a ring keep rotating to get the next task from a fixed position
class ring:

    current = None
    num_of_tasks_in_ring = 0

    def __init__(self, current: node = None) -> None:
        self.current = current

    def append(self, new_node: node) -> None:
        last = self.current.last
        last.next = new_node
        new_node.last = last
        new_node.next = self.current
        self.current.last = new_node

    def pop(self) -> Any:
        self.current.last.next = self.current.next
        self.current.next.last = self.current.last
        data = self.current.get()
        self.current = self.current.next
        return data

    @classmethod
    def is_empty(self) -> bool:
        return self.num_of_tasks_in_ring == 0

    # for iteration?
    def __iter__(self): pass
    def __next__(self): pass
    # when remove
    def __del__(self): pass
    # when try to access
    def __enter__(self): pass
    def __exit__(self, type, value, trace): pass


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


# lua table like strcture
class table:
    def __init__(self, node: node = None) -> None:
        pass

    def __keys__(self) -> None: pass
    def __iter__(self) -> None: pass
    def __next__(self) -> None: pass
    def __getitem__(self) -> None: pass


class task_container(stack, queue, ring):
    def __init__(self, root=None, current=None) -> None:
        stack.__init__(self, root)
        queue.__init__(self, root)
        ring.__init__(self, current)

    def append(self, node: node, target: str = "ring") -> None:
        match target:
            case "ring":
                pass
            case "queue":
                pass
            case "stack":
                pass
