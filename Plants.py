#from Plant import Plant
from Board import Board
from Board import Tile
import Constants

from time import sleep
import curses


stdscr = curses.initscr()
curses.noecho()
curses.cbreak()



# according to python docs: call these to restore settings
curses.nocbreak()
stdscr.keypad(False)
curses.echo()



# test printing a board and whatnot #############
# make this a function later

# init the board
board = Board()

# set cursor to not blink, as it's not needed
curses.curs_set(False)

# init colors 
curses.start_color()
curses.use_default_colors()


# addstr() forms: https://docs.python.org/3/howto/curses.html#displaying-text
"""
for row in range(Constants.BOARD_ROWS):
			for col in range(Constants.BOARD_COLUMNS):
				if col == 0:
					stdscr.addstr("\n")
				#self.tiles[row][col].display()
				if board.tiles[row][col].plant == None:
					stdscr.addstr(".")
				else:
					stdscr.addstr(board.tiles[row][col].plant.image)

"""
board.stdscr = stdscr
stdscr.addstr("Starting board...")
sleep(3)
board.display()
board.run(10)

#################################################

#wait for a key before ending the program
stdscr.getch()

# end curses
curses.endwin()








#non-curses code
"""
print("\nCreating the board")
board = Board()

print("\nAttempting to print board: ")
board.display()

print("\nAttempting to get active window name periodically")
from AppKit import NSWorkspace
#active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
#print(active_app_name)

for i in range(10):
	sleep(2)
	print(NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'])



"""