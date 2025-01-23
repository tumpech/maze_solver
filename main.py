from window import Window, Line, Point

def main():
    win = Window(800,600)
    line = Line(Point(20,20), Point(300,300))
    win.draw_line(line,"black")
    win.wait_for_close()

if __name__ == "__main__":
    main()
