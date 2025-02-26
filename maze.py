from cell import Cell
import time
import random

class Maze():
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed:
            random.seed(seed)

        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        self._cells = [
            [Cell(self._win) for y in range(self._num_rows)]
            for x in range(self._num_cols)]
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self,i,j):
        if self._win == None:
            return
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        self._cells[i][j].draw(x1,y1,x2,y2)
        #self._animate()
    
    def _animate(self):
        if self._win == None:
            return
        self._win.redraw()
        time.sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].top_wall = False
        self._draw_cell(0,0)
        self._cells[self._num_cols-1][self._num_rows-1].bottom_wall = False
        self._draw_cell(self._num_cols-1,self._num_rows-1)
    
    def _break_walls_r(self,i,j):
        self._cells[i][j].visited = True
        while True:
            next_index_list = []

            # find potential path
            # left
            if i > 0 and not self._cells[i-1][j].visited:
                next_index_list.append((i-1,j))
            
            # right
            if i < self._num_cols -1 and not self._cells[i+1][j].visited:
                next_index_list.append((i+1,j))
            
            # up
            if j > 0 and not self._cells[i][j-1].visited:
                next_index_list.append((i,j-1))
            
            # down
            if j < self._num_rows -1 and not self._cells[i][j+1].visited:
                next_index_list.append((i,j+1))
            
            # if we cannot go anywhere, break
            if len(next_index_list) == 0:
                self._draw_cell(i, j)
                break

            # choose a path from potential paths
            next_index = next_index_list[random.randrange(len(next_index_list))]
            
            # knock down wall for the path
            # right
            if next_index[0] == i+1:
                self._cells[i][j].right_wall = False
                self._cells[i+1][j].left_wall = False
            # left
            if next_index[0] == i-1:
                self._cells[i][j].left_wall = False
                self._cells[i-1][j].right_wall = False
            # up
            if next_index[1] == j-1:
                self._cells[i][j].top_wall = False
                self._cells[i][j-1].bottom_wall = False
            # down
            if next_index[1] == j+1:
                self._cells[i][j].bottom_wall = False
                self._cells[i][j+1].top_wall = False
            self._break_walls_r(next_index[0],next_index[1])
    
    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        return self._solve_r(0,0)
    
    def _solve_r(self,i,j):
        self._animate()
        self._cells[i][j].visited = True
        if i == self._num_cols - 1  and j == self._num_rows - 1:
            return True
        
        # check possible direction
        # right
        if i < self._num_cols -1 and not self._cells[i][j].right_wall and not self._cells[i+1][j].visited:
            self._cells[i][j].draw_move(self._cells[i+1][j])
            if self._solve_r(i+1,j):
                return True
            self._cells[i+1][j].draw_move(self._cells[i][j],undo=True)
        # down
        if j < self._num_rows -1 and not self._cells[i][j].bottom_wall and not self._cells[i][j+1].visited:
            self._cells[i][j].draw_move(self._cells[i][j+1])
            if self._solve_r(i,j+1):
                return True
            self._cells[i][j+1].draw_move(self._cells[i][j],undo=True)
        # left
        if i > 0 and not self._cells[i][j].left_wall and not self._cells[i-1][j].visited:
            self._cells[i][j].draw_move(self._cells[i-1][j])
            if self._solve_r(i-1,j):
                return True
            self._cells[i-1][j].draw_move(self._cells[i][j],undo=True)
        # up
        if j > 0 and not self._cells[i][j].top_wall and not self._cells[i][j-1].visited:
            self._cells[i][j].draw_move(self._cells[i][j-1])
            if self._solve_r(i,j-1):
                return True
            self._cells[i][j-1].draw_move(self._cells[i][j],undo=True)
        return False
