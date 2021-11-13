from graph import Graph, DirectedGraph
from graphutils import GraphUtils
from maze import Maze
from treeutils import TreeUtils
from tree import BinaryTree, Tree


def dfs_example():
    graph = Graph()

    # creating the example graph from wiiliam fiset DFS video
    # it's the 4th video in the graphs playlist it is shown at
    # timestamp 1:10
    for i in range(13):
        graph.add_node(str(i))

    print('\nThis is the graph we are working with')
    graph.add_edge("0", "1")
    graph.add_edge("0", "9")
    graph.add_edge("1", "8")
    graph.add_edge("9", "8")
    graph.add_edge("8", "7")
    graph.add_edge("7", "10")
    graph.add_edge("10", "11")
    graph.add_edge("11", "7")
    graph.add_edge("7", "6")
    graph.add_edge("7", "3")
    graph.add_edge("6", "5")
    graph.add_edge("5", "3")
    graph.add_edge("3", "2")
    graph.add_edge("3", "4")
    print(graph)

    print('DFS path starting at node 0.')
    print(GraphUtils.depth_first_traversal_iterative(graph, "0"))


def connected_components_example():
    graph = Graph()
    # creating the example graph from wiiliam fiset DFS video
    # it's the 4th video in the graphs playlist it is shown at
    # timestamp 5:09
    for i in range(18):
        graph.add_node(str(i))

    print('\nThis is the graph we are working with')
    graph.add_edge("0", "4")
    graph.add_edge("0", "13")
    graph.add_edge("0", "8")
    graph.add_edge("0", "14")
    graph.add_edge("8", "4")
    graph.add_edge("8", "14")
    graph.add_edge("13", "14")

    graph.add_edge("6", "11")
    graph.add_edge("6", "7")
    graph.add_edge("11", "7")

    graph.add_edge("5", "1")
    graph.add_edge("5", "16")
    graph.add_edge("5", "17")

    graph.add_edge("3", "9")
    graph.add_edge("15", "10")
    graph.add_edge("15", "2")
    graph.add_edge("15", "9")
    graph.add_edge("2", "9")
    print(graph)

    components = GraphUtils.find_components(graph)
    print("Here are the components in  the graph: \n", components)


def bfs_example():
    graph = Graph()
    # creating the example graph from wiiliam fiset BFS video
    # it's the 5th video in the graphs playlist it is shown at
    # timestamp 0:45
    for i in range(13):
        graph.add_node(str(i))

    print('\nThis is the graph we are working with')
    graph.add_edge("10", "1")
    graph.add_edge("10", "9")
    graph.add_edge("1", "8")
    graph.add_edge("9", "8")
    graph.add_edge("9", "0")
    graph.add_edge("0", "11")
    graph.add_edge("0", "7")
    graph.add_edge("7", "6")
    graph.add_edge("7", "3")
    graph.add_edge("7", "11")
    graph.add_edge("6", "5")
    graph.add_edge("3", "4")
    graph.add_edge("3", "2")
    graph.add_edge("8", "12")
    graph.add_edge("12", "2")
    print(graph)

    print(f'Here is the BFS path starting at node 0')
    print(GraphUtils.breadth_first_search(graph, '0'))

    print('\nThe shortest path from 0 to 12 : ', end="")
    print(GraphUtils.unweighted_shortest_path(graph, '0', '12'))


def maze_example():
    maze = Maze('maze_path_example.txt')
    maze.find_shortest_path()


def leaf_sum_example():
    # algorithms video it's the 8th video in the graphs playlist
    # creating the example tree from wiiliam fiset Begineer tree
    # it is shown at timestamp 1:00

    tree = Tree(5)
    tree.add_node(3)
    tree.add_node(4)
    tree.add_children(5, 4, 3)

    tree.add_node(-6)
    tree.add_node(1)
    tree.add_children(4, 1, -6)

    tree.add_node(7)
    tree.add_node(0)
    tree.add_node(-4)
    tree.add_children(3, 0, 7, -4)

    tree.add_node(9)
    tree.add_node(2)
    tree.add_children(1, 2, 9)

    tree.add_node(8)
    tree.add_children(7, 8)

    print('\nThis is the tree we are working with.\n')
    print(tree)

    print('Sum of leaf nodes = ', TreeUtils.leaf_nodes_sum(tree))


def tree_height_example():
    #        0
    #       / \
    #      1   2
    #     / \ / \
    #    3  4 5  6
    #   / \
    #  7   8
    tree = BinaryTree(0)

    tree.add_left_child(0, 1)
    tree.add_right_child(0, 2)

    tree.add_left_child(1, 3)
    tree.add_right_child(1, 4)

    tree.add_left_child(2, 5)
    tree.add_right_child(2, 6)

    tree.add_left_child(3, 7)
    tree.add_right_child(3, 8)

    print('\nThis is the tree we are working with.\n')
    print(tree)

    print('Height of tree = ', TreeUtils.height_of_tree(tree))


def rooting_tree_example():
    # creating the example tree from wiiliam fiset Rooting a tree
    # video it's the 9th video in the graphs playlist it is shown
    # at timestamp 0:30
    tree = Graph()
    for i in range(7):
        tree.add_node(i)

    tree.add_edge(4, 5)
    tree.add_edge(5, 6)
    tree.add_edge(5, 0)
    tree.add_edge(0, 1)
    tree.add_edge(0, 2)
    tree.add_edge(2, 3)

    print('\n\nThe is the tree before it is rooted at node 0.')
    print(tree)

    rooted_tree = TreeUtils.root_tree_on_node(tree, 0)
    print('\nTree rooted at node 0.')
    print(rooted_tree)


def center_node_example():
    # creating the example tree from wiiliam fiset tree center(s)
    # video it's the 10th video in the graphs playlist it is shown
    # at timestamp 2:40
    tree = Graph()
    for i in range(10):
        tree.add_node(i)

    tree.add_edge(0, 1)
    tree.add_edge(1, 3)
    tree.add_edge(1, 4)
    tree.add_edge(4, 5)
    tree.add_edge(4, 8)
    tree.add_edge(3, 2)
    tree.add_edge(3, 7)
    tree.add_edge(3, 6)
    tree.add_edge(6, 9)

    print('\nThe tree we are working with.\n')
    print(tree)

    print('Center node(s) of the tree :', TreeUtils.get_center_nodes(tree))


def center_node_example2():
    # creating the example tree from wiiliam fiset tree center(s)
    # video it's the 10th video in the graphs playlist it is shown
    # at timestamp 1:10
    tree = Graph()
    for i in range(10):
        tree.add_node(i)

    tree.add_edge(0, 1)
    tree.add_edge(1, 2)
    tree.add_edge(2, 9)
    tree.add_edge(2, 6)
    tree.add_edge(2, 3)
    tree.add_edge(3, 4)
    tree.add_edge(3, 5)
    tree.add_edge(6, 7)
    tree.add_edge(6, 8)

    print('\nThe tree we are working with.\n')
    print(tree)

    print('Center node(s) of the tree :', TreeUtils.get_center_nodes(tree))


def isomorphism_example():
    # creating the example trees from wiiliam fiset isomorphic trees
    # video it's the 11th video in the graphs playlist it is shown
    # at timestamp 5:07
    tree1 = Graph()
    tree2 = Graph()

    for i in range(6):
        tree1.add_node(i)
        tree2.add_node(i)

    tree1.add_edge(0, 1)
    tree1.add_edge(1, 2)
    tree1.add_edge(1, 4)
    tree1.add_edge(4, 3)
    tree1.add_edge(3, 5)

    tree2.add_edge(0, 1)
    tree2.add_edge(1, 2)
    tree2.add_edge(2, 4)
    tree2.add_edge(4, 3)
    tree2.add_edge(4, 5)

    print('\nThis are the trees we are working with :\n')
    print(tree1)
    print(tree2)
    print('These trees are isomorphic =',
          TreeUtils.are_isomorphic(tree1, tree2))


def main():
    dfs_example()
    connected_components_example()
    bfs_example()
    maze_example()
    leaf_sum_example()
    tree_height_example()
    rooting_tree_example()
    center_node_example()
    center_node_example2()
    isomorphism_example()


if __name__ == '__main__':
    main()
