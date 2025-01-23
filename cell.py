from graphics import Line, Point

class Cell():
    def __init__(self, window):
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.y2 = None
        self.__window = window
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True

    
    def draw(self, x1, y1, x2, y2):
        if self.__window == None:
            return
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.left_wall:
            line = Line(
                Point(self.__x1,self.__y1),
                Point(self.__x1,self.__y2))
            self.__window.draw_line(line)
        if self.right_wall:
            line = Line(
                Point(self.__x2,self.__y1),
                Point(self.__x2,self.__y2))
            self.__window.draw_line(line)
        if self.top_wall:
            line = Line(
                Point(self.__x1,self.__y1),
                Point(self.__x2,self.__y1))
            self.__window.draw_line(line)
        if self.bottom_wall:
            line = Line(
                Point(self.__x1,self.__y2),
                Point(self.__x2,self.__y2))
            self.__window.draw_line(line)
    
    def draw_move(self, to_cell, undo=False):
        if undo:
            color="grey"
        else:
            color="red"
        half_length = abs(self.__x2 - self.__x1) // 2
        x_center = half_length + self.__x1
        y_center = half_length + self.__y1
        startPoint = Point(x_center, y_center)

        half_length2 = abs(to_cell.__x2 - to_cell.__x1) // 2
        x_center2 = half_length2 + to_cell.__x1
        y_center2 = half_length2 + to_cell.__y1
        endPoint = Point(x_center2,y_center2)

        self.__window.draw_line(Line(startPoint,endPoint),color)
