import Constants

import random
import curses

class Coordinates:
	x = 0
	y = 0
	def __init__(self, newx = 0, newy = 0):
		self.x = newx
		self.y = newy
		return


class Plant:
	image = "@"

	#curses color curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
	color = curses.COLOR_RED # V.02
	coords = Coordinates(0, 0)


	def __init__(self, image="@"):
		self.image = image
		return

	def getStr(self):
		return (self.image + Constants.BOARD_SPACING)


	def setCoordinates(self, x, y):
		self.coords.x = x
		self.coords.y = y
		return

	# try: return a new plant object with coordinates
	# board reads the coordinates and places it based on
	# those

	# how to determine which direction:
	def step(self):
		# placeholder: 1/4 chance of growth
		if random.randint(0, 3) == 3:
			# now randomly select a square/coordinate to place it
			# choose random number in range of coordinates+1
			newGrowthCoords = Coordinates()
			newGrowthCoords.x = random.randint(self.coords.x-1, self.coords.x+1)
			newGrowthCoords.y = random.randint(self.coords.y-1, self.coords.y+1)
			return newGrowthCoords


		return None
			
