from graphics import Line, Point

class Cell():
    def __init__(self, window):
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.__window = window
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True

    
    def draw(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        if self.left_wall:
            line = Line(
                Point(self.x1,self.y1),
                Point(self.x1,self.y2))
            self.__window.draw_line(line)
        if self.right_wall:
            line = Line(
                Point(self.x2,self.y1),
                Point(self.x2,self.y2))
            self.__window.draw_line(line)
        if self.top_wall:
            line = Line(
                Point(self.x1,self.y1),
                Point(self.x2,self.y1))
            self.__window.draw_line(line)
        if self.bottom_wall:
            line = Line(
                Point(self.x1,self.y2),
                Point(self.x2,self.y2))
            self.__window.draw_line(line)
