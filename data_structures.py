

"""
This is the file I used to study Data Structures
and code my own versions of the following Data Structures:
    1.) Singly LinkedList
    2.) Stack (Python List Based)
    3.) Queue (Python deque based)
    4.) Tree (Binary Tree)
    5.) Graph (Hashmap/Dictionary Based)
"""


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return f'{self.data} -> {self.next}' if self.next else f'{self.data}'

    def __repr__(self):
        return f'{self.data} -> {self.next}' if self.next else f'{self.data}'

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, _nxt):
        self.next = _nxt


class LinkedList:

    def __init__(self):
        self.head = Node()

    def __str__(self):
        return f'LinkedList({self.head})'

    def __repr__(self):
        return f'LinkedList({self.head})'

    def new_head(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def pop_head(self):
        to_remove = self.head.get_data()
        self.head = self.head.get_next()
        return to_remove

    def new_data(self, data, parent):
        new_node = Node(data)
        current = self.head
        while current:
            if current.get_data() == parent:
                new_node.set_next(current.get_next())
                current.set_next(new_node)
                return
            current = current.get_next()
        raise Exception(f'Parent "{parent}" not in LinkedList.')

    def delete_data(self, data, parent):
        current = self.head
        while current:
            if current.get_data() == parent and current.get_next().get_data() == data:
                if current.get_next():
                    current.set_next(current.get_next().get_next())
                    return
                self.pop_head()
                return
            current = current.get_next()
        raise Exception(f'Parent "{parent}" with child node "{data}" doesn\'t exist in the LinkedList.')

    def new_tail(self, data):
        current = self.head
        while current.get_data() is not None:
            if current.get_next().get_data():
                current = current.get_next()
                continue
            new_node = Node(data)
            new_node.set_next(current.get_next())
            current.set_next(new_node)
            return
        self.new_head(data)

    def delete_tail(self):
        current = self.head
        while current.get_next().get_data() is not None:
            if current.get_next().get_next().get_data() is not None:
                current = current.get_next()
                continue
            to_return = current.get_next().get_data()
            current.set_next(current.get_next().get_next())
            return to_return
        if self.head.get_data() is not None:
            return self.pop_head()
        raise Exception('Empty LinkedList. Can\'t perform ".delete_tail()" method.')

    def reverse_linked_list(self):
        new_linked_list = LinkedList()
        current = self
        while current.head.get_data() is not None:
            new_linked_list.new_head(current.pop_head())
        self.head = new_linked_list.head
        del new_linked_list
        return self


class Stack:

    def __init__(self):
        self._items = []

    def __str__(self):
        return f'Stack({", ".join([str(item) for item in self._items])})'

    def __repr__(self):
        return self.__str__()

    def push(self, data):
        self._items.append(data)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1] if len(self._items) > 0 else None


from collections import deque as dq


class Queue:

    def __init__(self):
        self._items = dq()

    def __str__(self):
        return f"Queue({', '.join([str(item) for item in self._items])})"

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self._items)

    def enqueue(self, data):
        self._items.append(data)

    def deque(self):
        return self._items.popleft()


class TreeNode:

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'Node(Data={self.data}, Left={self.left}, Right={self.right})'

    def __repr__(self):
        return self.__str__()

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right


class BinaryTree:

    def __init__(self, root=None):
        self.root = TreeNode(root)

    def __str__(self):
        return f'BinaryTree({self.root})'

    def __repr__(self):
        return self.__str__()

    def insert(self, data):
        if self.root.get_data() is None:  # empty Tree
            return self.root.set_data(data)
        new_node = TreeNode(data)
        current = self.root
        while True:
            if data < current.get_data():
                if current.get_left() is None:
                    return current.set_left(new_node)
                current = current.get_left()
                continue
            elif data > current.get_data():
                if current.get_right() is None:
                    return current.set_right(new_node)
                current = current.get_right()
                continue
            return

    def delete(self, data):
        pass


class Graph:

    def __init__(self):
        self.nodes = {}

    def __str__(self):
        return "Graph(\n" + ',\n'.join([f'\t{key} => {value}' for key, value in self.nodes.items()]) + '\n)'

    def __repr__(self):
        return "Graph(\n" + ',\n'.join([f'\t{key} => {value}' for key, value in self.nodes.items()]) + '\n)'

    def __contains__(self, item):
        return item in self.nodes

    def number_of_nodes(self):
        return len(self.nodes)

    def get_connections_of(self, node):
        if node in self.nodes:
            return self.nodes[node]
        raise Exception(f'"{node}" not in this Graph.')

    def add_node(self, node, connections):
        if connections is None:
            connections = []
        if node not in self.nodes:
            self.nodes[node] = connections
            return
        raise Exception(f'"{node}" already in  the Graph. Just adding connections? Use .add_connections() instead')

    def add_connections(self, node, connections):
        try:
            if node in self.nodes:
                self.nodes[node].extend(list(connections))
                return
            raise Exception(f'"{node}" not in graph.')
        except TypeError:
            self.nodes[node].append(connections)

    def delete_node(self, node):
        try:
            for vertex in self.nodes:
                if node in self.get_connections_of(vertex):
                    self.nodes[vertex].remove(node)
            del self.nodes[node]
        except KeyError:
            pass

    def delete_connections(self, node):
        if node in self.nodes:
            self.nodes[node] = []
            return


# Track the visited nodes and the stack of nodes to visit
# pop an item from the stack
# check if not visited. If true, visit neighbors and add to stack
# if not, proceed.


def dfs_iteration(graph, vertex):
    _visited = []
    node_stack = [vertex]
    while len(node_stack) > 0:
        v = node_stack.pop()
        if v not in _visited:
            # mark visited and search neighbors
            _visited.append(v)
            for connection in graph.get_connections_of(v):
                if connection not in _visited:
                    node_stack.append(connection)
    return _visited


def pre_dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = []
    if start_vertex not in visited:
        visited.append(start_vertex)
        for connection in graph.get_connections_of(start_vertex):
            if connection not in visited:
                pre_dfs(graph, connection, visited)
    return visited


def post_dfs(graph, start_vertex, visited=None):
    if visited is None:
        visited = []
    if start_vertex not in visited:
        for connection in graph.get_connections_of(start_vertex):
            if connection not in visited:
                post_dfs(graph, connection, visited)
        visited.append(start_vertex)
    return visited


def bfs(graph, start_vertex):
    _visited = []
    node_queue = Queue()
    node_queue.enqueue(start_vertex)
    while len(node_queue) > 0:
        v = node_queue.deque()
        if v not in _visited:
            _visited.append(v)
            for connection in graph.get_connections_of(v):
                node_queue.enqueue(connection)
    return _visited


def invert_binary_tree(binary_tree, current_node):
    # base case: we're on leaf node
    if current_node.get_left() is None and current_node.get_right() is None:
        return

    # recursive case
    if current_node.get_left() is not None:
        invert_binary_tree(binary_tree, current_node.get_left())
    left, right = current_node.get_left(), current_node.get_right()
    current_node.set_left(right)
    current_node.set_right(left)
    if current_node.get_left() is not None:
        invert_binary_tree(binary_tree, current_node.get_left())
    return binary_tree


from collections import deque


def topological_sort(graph, start_vertex, visited=None):
    # Just implement a post DFS and inverse it to do
    # topological sort.
    if visited is None:
        visited = deque()
    if start_vertex not in visited:
        for connection in graph.get_connections_of(start_vertex):
            if connection not in visited:
                topological_sort(graph, connection, visited)
        visited.appendleft(start_vertex)
    return list(visited)


def main():
    my_graph = Graph()
    my_graph.add_node(1, [2, 3, 10])
    my_graph.add_node(2, [3])
    my_graph.add_node(3, [4, 6])
    my_graph.add_node(4, [6])
    my_graph.add_node(5, [])
    my_graph.add_node(6, [7])
    my_graph.add_node(7, [5])
    my_graph.add_node(8, [9])
    my_graph.add_node(9, [])
    my_graph.add_node(10, [9])
    print(my_graph)
    print(topological_sort(my_graph, 1))


if __name__ == '__main__':
    main()
