from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800,600)
    
    c1 = Cell(win)
    c1.left_wall = False
    c1.draw(20,20,170,170)

    c2 = Cell(win)
    c2.right_wall = False
    c2.draw(180,20,320,170)

    c3 = Cell(win)
    c3.top_wall = False
    c3.draw(20,180,170,320)

    c4 = Cell(win)
    c4.bottom_wall = False
    c4.draw(180,180,320,320)

    c1.draw_move(c2)
    c2.draw_move(c4)
    c4.draw_move(c2,undo=True)


    line = Line(Point(20,20), Point(300,300))
    win.draw_line(line,"black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
