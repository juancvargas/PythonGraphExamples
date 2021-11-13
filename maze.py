from collections import deque
from typing import Tuple


class Maze:
    START_SYMBOL = 'S'
    END_SYMBOL = 'E'
    ROCK_SYMBOL = '#'
    PATH_SYMBOL = '.'
    SHORTEST_PATH_MARKER = '!'

    def __init__(self, file: str):
        # copying the maze from the file into a matrix
        self._matrix = []
        with open(file, mode='r') as f:
            for line in f:
                row = list(line)
                # remove the '\n' at the end of the line
                row.pop()
                self._matrix.append(row)

        if len(self._matrix) < 1:
            raise ValueError('Text file didn\'t contain a maze.')

        self._NUM_ROWS = len(self._matrix)
        self._NUM_COLS = len(self._matrix[0])

        self._start_index = self._get_start_index()
        if self._start_index is None:
            raise ValueError('No start symbol "S" provided in the maze.')

    def _get_start_index(self) -> Tuple:
        """
        Return a tuple indicating the index of the Start Symbol in the grid.
        If the start symbol is not in the grid return None.
        """
        for i in range(self._NUM_ROWS):
            for j in range(self._NUM_COLS):
                if self._matrix[i][j] == self.START_SYMBOL:
                    return (i, j)

        return None

    def find_shortest_path(self) -> None:
        """
        Displays the maze with the shorest path from S to E marked with 
        a SHORTEST_PATH_MARKER character. Performs a BFS starting at the 
        start_index.
        """
        queue = deque([self._start_index])
        visited = set([self._start_index])
        reached_end = False

        # set the prev coordinate of the start position to None
        prev_table = {self._start_index: None}

        while len(queue) > 0:
            coordinate = queue.popleft()

            if self._matrix[coordinate[0]][coordinate[1]] == 'E':
                reached_end = True
                break

            self._explore_neighbors(coordinate, prev_table, visited, queue)

        if reached_end:
            # The coordinate variable will equal to the exit position only
            # when symbol "E" is found.
            self._show_reconstructed_path(prev_table, coordinate)
            return

        print('No path from S to E found!')
        self._print_maze()

    def _explore_neighbors(self, coordinate: tuple, prev_table: dict,
                           visited: set, queue: deque) -> None:
        """Add the neighbors of the cell at the coordinate in matrix to queue"""
        # direction vectors
        dr = [-1, 1, 0, 0]
        dc = [0, 0, 1, -1]

        for i in range(len(dr)):
            # coordinate tuple = (row, col)
            ncord = (coordinate[0] + dr[i], coordinate[1] + dc[i])

            # check if new coordinate is within bounds of the matrix
            if ncord[0] < 0 or ncord[1] < 0:
                continue
            if ncord[0] >= self._NUM_ROWS or ncord[1] >= self._NUM_COLS:
                continue

            # skip over none-path characters
            if ncord in visited:
                continue
            if self._matrix[ncord[0]][ncord[1]] == self.ROCK_SYMBOL:
                continue

            queue.append(ncord)
            visited.add(ncord)
            prev_table[ncord] = coordinate

    def _show_reconstructed_path(self, prev_table: dict, end_position: tuple) -> None:
        """
        Backtrack from end position to start position which is the shortest 
        path from start to end and mark all the cells along that path with  
        the SHORTEST_PATH_MARKER symbol. 
        """
        coord = end_position
        while coord is not None:
            self._matrix[coord[0]][coord[1]] = self.SHORTEST_PATH_MARKER
            coord = prev_table[coord]

        prompt = f'\nShortest path from {self.START_SYMBOL} to ' + \
            f'{self.END_SYMBOL} is marked with {self.SHORTEST_PATH_MARKER}'
        print(prompt, end='\n\n')
        self._print_maze()

    def _print_maze(self) -> None:
        for row in range(self._NUM_ROWS):
            for col in range(self._NUM_COLS):
                print(self._matrix[row][col], end="")
            print()  # need a newline after each row
