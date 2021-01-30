"""
This is the main script that it will run from
"""
# Import Modules
import random, math
from tkinter import *
# My Modules
from game import *
from players import *
from teams import *
from tournament import *
from objects import *
from season import *


class Window(Frame):
	game = Game([threeTeam1, threeTeam2], 21, 'winners', True)
	def __init__(self, master=None):
		# Parameters from Frame Class
		Frame.__init__(self, master)
		# Reference to master widget which is TK window
		self.master = master
		# Run init_window next
		self.initWindow()
	# Init Window
	def initWindow(self):

		# Changing Title of Master Window
		self.master.title("GAME")
		
		# Allowing the widget to take the full space of the root window
		self.pack(fill=BOTH, expand=1)
		
		playButton = Button(self, text='Play', command=self.play)
		playButton.place(x = 0, y = 50)
		# creating button instance
		quitButton = Button(self, text='Quit', command=self.clientExit)

		# Placing Button
		quitButton.place(x = 0, y = 10)


	def clientExit(self):
		exit()
	def play(self):
		winner = self.game.playGame()
		text = "{} wins with {} points!".format(winner.name, winner.statsPoints)
		win = Label(self, text=text)
		win.pack()


def main():
	#game = Game([threeTeam1, threeTeam2], 21, 'winners', True)
	#root = Tk()
	#root.geometry("600x300")
	#app = Window(root)
	#root.mainloop()
	season1 = Season(teamsThrees)
	menu = Menu(threeTeam4, season1)
	menu.seasonMenu
	x = input(">> ")

main()