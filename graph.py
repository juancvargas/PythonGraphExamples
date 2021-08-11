"""
Impementations of undirected and directed graphs.

@classes:

Graph: is an implementation of an undirected graph
DirectedGraph: is an implementation of a directed graph

Both implementations can also have weighted edges by passing a
weight as an optional third argument to the add_edge() method
when creating an edge between two nodes.
"""


from typing import Any


class _Node:
    def __init__(self, value: Any):
        self.value = value
        self._edges = []

    def add_edge(self, to_node: '_Node', weight: int):
        self._edges.append(_Edge(self, to_node, weight))

    def has_edge(self, to_node: '_Node'):
        for edge in self._edges:
            if edge.to_node == to_node:
                return True
        return False

    def remove_edge(self, edge: '_Edge'):
        self._edges.remove(edge)

    @property
    def edges(self) -> list['_Edge']:
        return self._edges

    @property
    def neighbors(self) -> list['_Node']:
        """Return a list with the neighbors of the node"""
        return [edge.to_node for edge in self._edges]

    def __str__(self) -> str:
        return f'Node({self.value})'

    def __repr__(self) -> str:
        return f'Node({self.value})'


class _Edge:
    def __init__(self, from_node: _Node, to_node: _Node, weight: int):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def __str__(self) -> str:
        return f'Node({self.from_node.value}) -> Node({self.to_node.value})'

    def __repr__(self) -> str:
        return f'Node({self.from_node.value}) -> Node({self.to_node.value})'


class Graph:
    '''
    Undirected graph implemented using an adjacency list.
    Nodes must be unique and edges have a default weight of 1.
    '''
    _DEFAULT_WEIGHT = 1

    def __init__(self, unweighted=True):
        self._nodes = {}
        self._is_unweighted = unweighted
        self._nodes_count = 0
        self._edges_count = 0

    def add_node(self, value: Any):
        if value not in self._nodes:
            self._nodes[value] = _Node(value)
            self._nodes_count += 1

    def remove_node(self, value: Any):
        node_to_remove = self._nodes.get(value)

        if node_to_remove == None:
            raise ValueError(f'Node {value} not in graph.')

        for node in self._nodes.values():
            for edge in node.edges:
                if edge.to_node == node_to_remove:
                    node.remove_edge(edge)
                    self._edges_count -= 1
                    break

        self._nodes.pop(value)
        self._nodes_count -= 1

    def has_node(self, value: Any):
        return value in self._nodes

    def get_node(self, value: Any):
        node = self._nodes.get(value)

        if node == None:
            raise ValueError(f'Node {value} not in graph')

        return node

    def add_edge(self, from_value: Any, to_value: Any, weight=_DEFAULT_WEIGHT):
        from_node = self._nodes.get(from_value)
        to_node = self._nodes.get(to_value)
        added_edge = False

        if from_node == None or to_node == None:
            missing_node = to_value if to_node is None else from_value
            raise ValueError(f'Node {missing_node} is not in graph.')

        # undirected graph need edges pointing in both directions
        if not from_node.has_edge(to_node):
            from_node.add_edge(to_node, weight)
            added_edge = True

        if not to_node.has_edge(from_node):
            to_node.add_edge(from_node, weight)
            added_edge = True

        self._edges_count += 1 if added_edge else 0

    def remove_edge(self, from_value: Any, to_value: Any):
        from_node = self._nodes.get(from_value)
        to_node = self._nodes.get(to_value)

        if from_node == None or to_node == None:
            missing_node = to_value if to_node is None else from_value
            raise ValueError(f'Node {missing_node} is not in graph.')

        for edge in from_node.edges:
            if edge.to_node == to_node:
                from_node.remove_edge(edge)
                self._edges_count -= 1
                break

    def has_edge(self, from_value: Any, to_value: Any) -> bool:
        from_node = self._nodes.get(from_value)
        to_node = self._nodes.get(to_value)

        if from_node == None or to_node == None:
            return False

        return from_node.has_edge(to_node)

    def size(self) -> int:
        return len(self._nodes)

    def is_tree(self) -> bool:
        return self._edges_count == self._nodes_count - 1

    def is_unweighted(self):
        return self._is_unweighted

    def __str__(self):
        output = ''
        for node in self._nodes.values():
            output += f'Node {node.value} is connected to ['
            str_list = [str(neighbor) for neighbor in node.neighbors]
            neighbors = ','.join(str_list)
            output += neighbors + ']\n' if len(str_list) > 0 else ']\n'

        return output

    def __iter__(self):
        self.nodes_iter = iter(self._nodes.values())
        return self.nodes_iter

    def __next__(self):
        return next(self.nodes_iter)


class DirectedGraph(Graph):
    '''
    Directed graph implemented using an adjacency list.
    Inherits most of it's methods from Graph class.
    Nodes must be unique and edges have a default weight of 1.
    '''
    _DEFAULT_WEIGHT = 1

    def __init__(self, unweighted=True):
        super().__init__(unweighted=unweighted)

    def add_edge(self, from_value: Any, to_value: Any, weight=_DEFAULT_WEIGHT):
        from_node = self._nodes.get(from_value)
        to_node = self._nodes.get(to_value)

        if from_node == None or to_node == None:
            raise ValueError

        if not from_node.has_edge(to_node):
            from_node.add_edge(to_node, weight)
