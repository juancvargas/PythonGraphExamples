from typing import Any, Iterable


class Tree:
    """Implementation of a rooted tree using an adjacency list."""
    class _Node:
        def __init__(self, value: Any) -> None:
            self.value = value
            self._children = set()

        def add_child(self, node: 'Tree._Node') -> None:
            """Add node to this nodes set of children"""
            if node not in self._children:
                self._children.add(node)

        def remove_child(self, node: 'Tree._Node') -> None:
            """Remove a child from the nodes set if children"""
            if node in self._children:
                self._children.remove(node)

        @property
        def children(self) -> set['Tree._Node']:
            """Return the children set of the node"""
            return self._children

        def __str__(self) -> str:
            return f'Node({self.value})'

        def __repr__(self) -> str:
            return f'Node({self.value})'

    def __init__(self, root_value: Any) -> None:
        self._root = self._Node(root_value)
        self._nodes = {root_value: self._root}

    def add_node(self, value: Any) -> bool:
        """Return boolean indicating if node with value was added to the tree"""
        if value in self._nodes:
            return False

        self._nodes[value] = self._Node(value)
        return True

    def add_children(self, start: Any, *nodes: Iterable[Any]) -> None:
        """Add directed edge from node1 to every node in nodes"""
        start_node = self._nodes.get(start)

        if start_node is None:
            raise ValueError(f'node {start_node.value} not in tree')

        for node in nodes:
            if node not in self._nodes:
                raise ValueError(f'node {node} not in tree')

            start_node.add_child(self._nodes.get(node))

    @property
    def root(self) -> _Node:
        return self._root

    def get_node(self, value: Any) -> _Node:
        node = self._nodes.get(value)

        if node is None:
            raise ValueError(f'Node {value} not in tree')

        return node

    def __str__(self) -> str:
        output = ''
        for node in self._nodes.values():
            output += f'Node {node.value}\'s children are ['
            str_list = [str(child) for child in node.children]
            children = ','.join(str_list)
            output += children + ']\n' if len(str_list) > 0 else ']\n'

        return output


class BinaryTree:
    """Implementation of a binary tree"""
    class _Node:
        def __init__(self, value: Any) -> None:
            self.value = value
            self.left = None
            self.right = None

        @property
        def children(self):
            """
            Return a list of strings representing a child of the node with the
            given value.
            """
            return [str(self.left), str(self.right)]

        def __str__(self) -> str:
            return f'Node({self.value})'

        def __repr__(self) -> str:
            return f'Node({self.value})'

    def __init__(self, root_value: Any) -> None:
        self._root = self._Node(root_value)
        self._nodes = {root_value: self._root}

    @property
    def root(self):
        return self._root

    def add_left_child(self, node_value: Any, left_value: Any):
        node = self._nodes.get(node_value)

        if node is None:
            raise ValueError(f'node {node_value} is not in the tree')

        left_node = self._Node(left_value)
        self._nodes[left_value] = left_node
        node.left = left_node

    def add_right_child(self, node_value: Any, right_value: Any):
        node = self._nodes.get(node_value)

        if node is None:
            raise ValueError(f'node {node_value} is not in the tree')

        right_node = self._Node(right_value)
        self._nodes[right_value] = right_node
        node.right = right_node

    def __str__(self) -> str:
        output = ''
        for node in self._nodes.values():
            output += f'Node {node.value}\'s children are ['
            str_list = [str(child) for child in node.children]
            children = ','.join(str_list)
            output += children + ']\n' if len(str_list) > 0 else ']\n'

        return output
