import os
import curses

# init curses
stdscr = curses.initscr()
stdscr.keypad(True)
stdscr.nodelay(True)
curses.noecho()
curses.cbreak()
curses.curs_set(False)

maxlines, maxcols = curses.LINES - 1, curses.COLS - 1
centerx, centery = maxlines // 2, maxcols // 2

# game logic
def main():
    def draw():
        stdscr.addstr(centerx, centery, "Hello Curses")
        stdscr.refresh()

    running = True
    while running:
        try:
            key = stdscr.getkey()
        except:
            key = " "

        if key == "q":
            running = False
        
        draw()

try:
    main()
finally:
    # end curses
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    os.system("clear")
