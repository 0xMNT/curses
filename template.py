import os
import curses

# init curses
stdscr = curses.initscr()
stdscr.keypad(True)
stdscr.nodelay(True)
curses.noecho()
curses.cbreak()
curses.curs_set(False)

max_lines, max_cols = curses.LINES - 1, curses.COLS - 1
center_x, center_y = max_lines // 2, max_cols // 2

# game logic
def main():
    def draw():
        stdscr.addstr(center_x, center_y, "Hello Curses")
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
