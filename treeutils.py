from typing import Any
from graph import DirectedGraph, Graph, _Node
from tree import BinaryTree, Tree


class TreeUtils:
    @classmethod
    def leaf_nodes_sum(cls, tree: Tree) -> int:
        """Return the sum of all the leaf nodesof the tree"""
        if tree is None or not isinstance(tree, Tree):
            raise ValueError('Argument not a tree.')

        return cls._leaf_sum_helper(tree.root, 0)

    @classmethod
    def _leaf_sum_helper(cls, node: Tree._Node, sum: int):
        """
        Perform a DFS starting at the node. If node is a leaf return node.value
        else return the sum of all the leaf nodes of that nodes subtrees.
        """
        if cls._is_leaf(node):
            return node.value

        for child in node.children:
            sum += cls._leaf_sum_helper(child, 0)

        return sum

    @classmethod
    def _is_leaf(cls, node: Tree._Node):
        return len(node.children) == 0

    @classmethod
    def height_of_tree(cls, tree: BinaryTree) -> int:
        """Return the height of the tree"""
        if tree is None or not isinstance(tree, BinaryTree):
            raise ValueError('Argument not a binary tree')

        return cls._height_helper(tree.root)

    @classmethod
    def _height_helper(cls, node: BinaryTree._Node) -> int:
        # Return -1 to correct for the height
        if node is None:
            return -1

        return max(cls._height_helper(node.left),
                   cls._height_helper(node.right)) + 1

    @classmethod
    def root_tree_on_node(cls, tree: Graph, node_value: Any) -> Tree:
        """
        Root the graph/tree at the node specified.

        Return a rooted Tree object.
        """
        if tree is None or not isinstance(tree, Graph) or not tree.is_tree():
            raise ValueError('Argument not a acyclic graph object(tree)')

        directed_tree = Tree(node_value)
        cls._build_tree(tree.get_node(node_value), None, directed_tree)

        return directed_tree

    @classmethod
    def _build_tree(cls, node: _Node, parent: _Node, tree: Tree) -> None:
        """
        Traverse the tree in a DFS manner starting at the node. Create a
        directed tree along the way.
        """
        for child in node.neighbors:
            # prevents infinite recursive calls by making sure that
            # child doesn't call it's parent recursively since the
            # edges are undirected
            if parent is not None and parent == child:
                continue
            tree.add_node(child.value)
            tree.add_children(node.value, child.value)
            cls._build_tree(child, node, tree)

    @classmethod
    def get_center_nodes(cls, tree: Graph) -> list:
        """
        Get the center(s) of the tree by iteratively removing leaf nodes until
        the center nodes are found.

        Return a list with the center nodes.
        """
        if tree is None or not isinstance(tree, Graph) or not tree.is_tree():
            raise ValueError('Argument not a acyclic graph object(tree)')

        NUM_NODES = tree.size()
        degree = {}
        leaves = []

        # populate the degrees table and find first leaf nodes layer
        for node in tree:
            degree[node] = len(node.edges)
            if degree[node] <= 1:
                leaves.append(node)
                degree[node] -= 1

        processed_leaves = len(leaves)
        while processed_leaves < NUM_NODES:
            new_leaves = []
            for leaf_node in leaves:
                for neighbor in leaf_node.neighbors:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        new_leaves.append(neighbor)
                degree[leaf_node] = 0  # "pruning/removing" the node
            processed_leaves += len(new_leaves)
            leaves = new_leaves

        return leaves  # center(s)

    @classmethod
    def are_isomorphic(cls, tree1: Graph, tree2: Graph):
        """
        Return a boolean indicating if the two trees are isomorphic

        @params must be undirected trees implemented using Graph objects
        """
        if not (isinstance(tree1, Graph) and isinstance(tree2, Graph)) \
                or not (tree1.is_tree() and tree2.is_tree()):
            raise ValueError('One of the inputs are not trees')

        tree1_centers = cls.get_center_nodes(tree1)
        tree2_centers = cls.get_center_nodes(tree2)

        tree1_rooted = cls.root_tree_on_node(tree1, tree1_centers[0].value)
        tree1_encoded = cls._ahu_encoding(tree1_rooted)

        # must compare against every center node of tree2
        for center in tree2_centers:
            tree2_rooted = cls.root_tree_on_node(tree2, center.value)
            tree2_encoded = cls._ahu_encoding(tree2_rooted)

            if tree1_encoded == tree2_encoded:
                return True

        return False

    @classmethod
    def _ahu_encoding(cls, root_tree: Tree):
        """AHU algorithm encoding implementation to serialize rooted tree"""
        return cls._ahu_helper(root_tree.root)

    @classmethod
    def _ahu_helper(cls, node: Tree._Node):
        """Implements the recursion for _ahu_encoding method"""
        if node is None:
            return ""

        labels = []
        for child in node.children:
            labels.append(cls._ahu_helper(child))

        # lexicographic sort
        labels.sort()

        return f'({"".join(labels)})'
