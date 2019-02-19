import random
import curses

s = curses.initscr()
curses.curs_set(0)
sh, sw = s.getmaxyx()

w = curser.newwin(sh, sw, 0, 0)
w.keypad(1)
w.timeout(100)