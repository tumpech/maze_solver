from graphics import Line, Point

class Cell():
    def __init__(self, window=None):
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._window = window
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.visited = False
    
    def draw(self, x1, y1, x2, y2):
        if self._window == None:
            return
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.left_wall:
            color = "black"
        else:
            color = "white"
        line = Line(
            Point(self._x1,self._y1),
            Point(self._x1,self._y2))
        self._window.draw_line(line,color)
        if self.right_wall:
                color = "black"
        else:
            color = "white"
        line = Line(
            Point(self._x2,self._y1),
            Point(self._x2,self._y2))
        self._window.draw_line(line,color)
        if self.top_wall:
            color = "black"
        else:
            color = "white"
        line = Line(
            Point(self._x1,self._y1),
            Point(self._x2,self._y1))
        self._window.draw_line(line,color)
        if self.bottom_wall:
            color = "black"
        else:
            color = "white"
        line = Line(
            Point(self._x1,self._y2),
            Point(self._x2,self._y2))
        self._window.draw_line(line,color)
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            color="grey"
        else:
            color="red"
        half_length = abs(self._x2 - self._x1) // 2
        x_center = half_length + self._x1
        y_center = half_length + self._y1
        startPoint = Point(x_center, y_center)

        half_length2 = abs(to_cell._x2 - to_cell._x1) // 2
        x_center2 = half_length2 + to_cell._x1
        y_center2 = half_length2 + to_cell._y1
        endPoint = Point(x_center2,y_center2)

        self._window.draw_line(Line(startPoint,endPoint),color)
