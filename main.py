from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800,600)
    
    c = Cell(win)
    c.left_wall = False
    c.draw(20,20,170,170)

    c = Cell(win)
    c.right_wall = False
    c.draw(180,20,320,170)

    c = Cell(win)
    c.top_wall = False
    c.draw(20,180,170,320)

    c = Cell(win)
    c.bottom_wall = False
    c.draw(180,180,320,320)

    line = Line(Point(20,20), Point(300,300))
    win.draw_line(line,"black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
