from typing import Dict, List
from graph import Graph, DirectedGraph, _Node
from collections import deque


class GraphUtils:
    @classmethod
    def depth_first_traversal_iterative(cls, graph: Graph, node: str) -> List:
        """
        Using a stack for this iterative implementation of DFS.

        Returns a list with a DFS traversal of the graph starting at node
        """
        stack = []
        visited = set()
        path = []

        if not graph.has_node(node):
            raise ValueError(f'Graph doesn\'t contain node {node}')

        stack.append(graph.get_node(node))

        while len(stack) > 0:
            current = stack.pop()

            if current in visited:
                continue

            path.append(current.value)
            visited.add(current)

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)

        return path

    @classmethod
    def depth_first_traversal_recursive(cls,  graph: Graph, node: str) -> List:
        """Returns a list with a DFS traversal of the graph starting at node"""
        if not graph.has_node(node):
            raise ValueError(f'Graph doesn\'t contain node {node}')

        path = []
        cls._dfs_helper(graph.get_node(node), set(), path)

        return path

    @classmethod
    def _dfs_helper(cls, node: _Node, visited: set, path: list) -> None:
        """Recursive helper function for DFS method"""
        path.append(node.value)
        visited.add(node)

        for neighbor in node.neighbors:
            if neighbor not in visited:
                cls._dfs_helper(neighbor, visited, path)

    @classmethod
    def find_components(cls,  graph: Graph) -> List[List]:
        """
        Return a list of lists were each of these list represents a connected component.
        """

        # This list will store tuples of node and the id of the component
        # that that node in the graph belongs to.
        nodes_ids = []
        num_components = 0
        visited = set()

        for node in graph:
            if not node in visited:
                cls._dfs_components(num_components, node, visited, nodes_ids)
                num_components += 1

        components = [[] for i in range(num_components)]
        for node, component_id in nodes_ids:
            components[component_id].append(node.value)

        return components

    @classmethod
    def _dfs_components(cls, component_id: int, node: _Node, visited: set,
                        ids_list: list) -> None:
        """
        Method finds the connected components in a graphs by doing a dfs
        of every node. It labels all the connected nodes with the same id.

        Populates the ids_list this list stores tuples of node and the id of the component that that node in the graph belongs to.
        """
        ids_list.append((node, component_id))
        visited.add(node)

        for neighbor in node.neighbors:
            if neighbor not in visited:
                cls._dfs_components(component_id, neighbor, visited, ids_list)

    @classmethod
    def breadth_first_search(cls, graph: Graph, node: str,
                             returnPrev: bool = False) -> List:
        """Returns a list indicating the BFS path rooted at the node"""
        if not graph.has_node(node):
            raise ValueError('Node not in graph!')

        start_node = graph.get_node(node)

        visited = set()
        visited.add(start_node)

        path = [start_node.value]

        queue = deque([start_node])
        while len(queue) > 0:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if not neighbor in visited:
                    queue.append(neighbor)
                    path.append(neighbor.value)
                    visited.add(neighbor)

        return path

    @ classmethod
    def unweighted_shortest_path(cls, graph: Graph, start: str, end: str) -> List:
        """
        Return a list with the shortest path from start node to end node

        Note: Function only works for unweighted graphs.
        """
        if not graph.is_unweighted():
            raise ValueError('Function only works for unweighted graphs.')

        if not (graph.has_node(start) and graph.has_node(end)):
            raise ValueError(f'Node {start} or node {end} not in graph.')

        start_node = graph.get_node(start)
        end_node = graph.get_node(end)

        prev_table = cls._get_prev_table(graph, start_node)

        return cls._reconstruct_path(start_node, end_node, prev_table)

    @ classmethod
    def _get_prev_table(cls, graph: Graph, start_node: _Node) -> Dict:
        """
        Return a dictionary where key is a graph Node object value and value
        is the parent value of that node in a BFS traversal starting
        at the start_node
        """
        queue = deque([start_node])

        visited = set()
        visited.add(start_node)

        # set the parent of the start node to None
        prev_table = {start_node.value: None}

        while len(queue) > 0:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
                    prev_table[neighbor.value] = current.value

        return prev_table

    @ classmethod
    def _reconstruct_path(cls, start: _Node, end: _Node, prev_table: dict) -> List:
        """
        @param start_node : starting node of the path
        @param end_node : ending node of the path
        @param prev_table : map where key is a node value and value is the
        parent value of that node.

        Return a list representing the path from start node to end node
        """
        path = []

        current = end.value
        while current is not None:
            path.append(current)
            current = prev_table[current]

        path.reverse()

        # If start and end are connected return the path
        return path if path[0] == start.value else []
