"""
This is the module to handle tournaments
So the basic rules of tournaments are that:
1) Has to be even number of teams -- Actually Power of 2
2) Each time half the teams lose
3) Ends when one team loses
FOr my first iteration, ill just have set positions for teams until it is correct
Then ill add randomization
"""
import random
from game import *

class Tournament:
	losers = []
	inPlay = []
	def __init__(self, teams, limit):
		self.teams = teams
		self.limit = limit
	def add(self, team):
		if isinstance(team, list):
			for player in team:
				self.teams.append(player)
				self.inPlay.append(player)
		else:
			self.teams.append(team)
			self.inPlay.append(team)
	def remove(self, team):
		self.teams.remove(team)
	def reset(self):
		self.teams.clear()
		self.inPlay.clear()
		self.losers.clear()
	def checkNumber(self):
		""" Check if even number of teams """
		numberOfTeams = len(self.teams)
		while numberOfTeams != 0 and (numberOfTeams % 2) == 0:
			numberOfTeams /= 2
		if numberOfTeams != 1:
			return False
		else:
			return True
	def setup(self):
		for player in self.teams:
			if player not in self.inPlay:
				self.inPlay.append(player)
		length = len(self.inPlay)
		print("Today we have a tournament between {} teams!\n".format(length))
	def matchUp(self, index):
		second = index + 1
		match = [self.inPlay[index], self.inPlay[second] ]
		return match
	def match(self, versus):
		game = Game([versus[0], versus[1]], self.limit, 'winners')
		winner = game.exhibition()
		for player in versus:
			if winner is player:
				pass
			else:
				loser = player
		print("{} is the winner! {} loses the game!".format(winner.name, loser.name))
		self.losers.append(loser)
		self.inPlay.remove(loser)
	def round(self):
		length = len(self.inPlay)
		half = length / 2
		index = 0
		while len(self.inPlay) != half:
			versus = self.matchUp(index)
			self.match(versus)
			index += 1
	def placing(self):
		place = 1
		print("Here is the Placing of teh Tournament:")
		places = sorted(self.teams, key=lambda team: team.statsWins, reverse=True)
		x = 1
		for team in places:
			print("{}. {} -- | {} wins | | {} losses |".format(x, team.name, team.statsWins, team.statsLosses))
			x += 1
	def seeding(self):
		""" Seeds the torunament by shuffling the order 5 times """
		x = 5
		while x != 0:
			random.shuffle(self.inPlay)
			x -= 1
	def tourney(self):
		""" Single Elimination Tournament """
		# FIrst check
		if self.checkNumber() == True:
			print("Valid tournament!")
			self.setup()
			self.seeding()
			x = 1
			while len(self.inPlay) != 1:
				print("\nRound {}:".format(x))
				self.round() 
				x += 1
			print("\n{} is the winner of the entire tournament! Congratulations!".format(self.inPlay[0]))
			self.placing()
			print("Here are the stats of the winner:")
			self.inPlay[0].seasonStats()
			print("Tournament end")
		else:
			print("Not even number of teams! Invalid tournament")
	def scoreCheck(self, team1, team2):
		score = team1
		if team2 > team1:
			score = team2
		return score
	def multiMatch(self, versus, bestOf):
		""" Match for a best of series """
		game = Game([versus[0], versus[1]], self.limit, 'winners')
		team1 = 0
		team2 = 0
		winningMark = math.ceil(bestOf / 2)
		while self.scoreCheck(team1, team2) < winningMark:
			winner = game.exhibition()
			if winner is versus[0]:
				team1 += 1
			else:
				team2 += 1

		if team1 > team2:
			winner = versus[0]
			loser = versus[1]
		else:
			winner = versus[1]
			loser = versus[0]
		print("{} is the winner! {} loses this match up!".format(winner.name, loser.name))
		self.losers.append(loser)
		self.inPlay.remove(loser)
	def multiRound(self, bestOf):
		length = len(self.inPlay)
		half = length / 2
		index = 0
		while len(self.inPlay) != half:
			versus = self.matchUp(index)
			self.multiMatch(versus, bestOf)
			index += 1
	def multiTourney(self, bestOf):
		""" Multi Elimination Tournament """
		# FIrst check
		if self.checkNumber() == True:
			print("Valid tournament!")
			self.setup()
			self.seeding()
			x = 1
			while len(self.inPlay) != 1:
				print("\nRound {}:".format(x))
				self.multiRound(bestOf) 
				x += 1
			print("\n{} is the winner of the entire tournament! Congratulations!".format(self.inPlay[0]))
			self.placing()
			print("Here are the stats of the winner:")
			self.inPlay[0].seasonStats()
			print("Now for the rest of the teams stats:")
			for player in self.losers:
				player.seasonStats()
			print("Tournament end")
		else:
			print("Not even number of teams! Invalid tournament")


