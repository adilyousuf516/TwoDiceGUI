""" 
Program: two_diceGUI.py
Author: Adil Yousuf 07/18/2023

GUI-based version of the Two Dice game which compares random numbers and provides the game's outcome.

NOTE: the file breezypythongui.py MUST be in the same directory as this file for the app to run correctly!
"""


from breezypythongui import EasyFrame
import random 
from tkinter.font import Font

# Other imports go here

#Class header
class TwoDiceGUI(EasyFrame):
	# Definition of our class constructor method
	def __init__ (self):
		EasyFrame.__init__(self, title = "Two Dice Game", width = 340, height = 280, resizable = False, background = "seagreen")

		# Add the various components to the window
		self.addLabel(text = "Two Dice Game", row = 0, column = 0, columnspan = 2, sticky = "NEWS", background = "seagreen", font = Font(family = "Impact", size = 24))

		
		self.addLabel(text = "Player's Roll is:  ", row = 1 , column = 0, background = "seagreen", sticky = "NE")
		self.playerRoll = self.addIntegerField(value = 0, row = 1, column = 1, width = 4, state = "readonly", sticky ="NW")
 
		


		self.addLabel(text = "Computer Roll is: ", row = 2, column = 0,  background = "seagreen", sticky = "NE")
		self.computerRoll = self.addIntegerField(value =0, row = 2, column = 1, width = 4, state = "readonly", sticky = "NW")



		self.button = self.addButton(text = "Roll Dice!", row = 3, column = 0, columnspan = 2, command = self.roll)
		self.button["background"] = "green"



		self.resultArea = self.addLabel(text = "", row = 4, column = 0, columnspan = 2, background = "seagreen", foreground = "yellow", font = Font(family = "Georgia", size = 15, weight = "bold"), sticky = "NEWS")

	# Definition of the roll() function
	def roll(self):
		#Variables for this function 
		playerDie = random.randint(1, 6)
		compDie = random.randint(1, 6)
		
		# Processing phase
		if playerDie > compDie:
			result = "Congratulations, you win!"
			self.resultArea["foreground"] = "yellow"
		elif playerDie < compDie:
			result = "Sorry, you lost..."
			self.resultArea["foreground"] = "red"
		else:
			result = "We have a tied."
			self.resultArea["foreground"] = "white"

		#output phase
		self.playerRoll.setNumber(playerDie)
		self.computerRoll.setNumber(compDie)
		self.resultArea["text"] = result


# Global definition of the main() method
def main():
	TwoDiceGUI().mainloop()

#Global call to main() for program entry
if __name__ == '__main__':
	main()