""" 
This module will have all classes and functions related to the different teams
"""
import math, random
from stats import *

class Team(Stats):
	# Team VS stats
	schedule = []

	def __init__(self, name, players):
		self.name = name
		self.players = players
	def __repr__(self):
		text = "{} {}: {}".format(self.first, self.last, self.overall)
		return text
	@property
	def teamAverage(self):
		self._teamAverage = 0
		numb = len(self.players)
		for player in self.players:
			self._teamAverage += player.overall
		self._teamAverage = math.ceil(self._teamAverage / numb)
		return self._teamAverage
	def __str__(self):
		return ("-- The {} --\nRated: {}".format(self.name, self.teamAverage))
	def showStats(self):
		print(" -- || The {} || --".format(self.name))
		self.statLine()
	def roster(self):
		print("{}'s Roster:".format(self.name))
		for player in self.players:
			print(player)
		print("Team Average: {}".format(self.teamAverage)) 
	def checkPosession(self):
		for player in self.players:
			if player.posession is True:
				return True
	def chooseBallHandler(self):
		player = random.choice(self.players)
		player.posession = True
		return player
	def chooseMember(self):
		member = random.choice(self.players)
		return member
	def rebounder(self):
		""" Chooses a rebounder both based on skill and luck """
		rebounderChance = 1
		rebounder = self.players[0]
		for player in self.players:
			playerChance = math.ceil(player.rebound * random.random())
			if playerChance > rebounderChance:
				rebounder = player
				rebounderChance = playerChance

		return rebounder
	def passerCheck(self):
		for player in self.players:
			if player.passed == 1:
				player.statsAssists += 1
				self.statsAssists += 1
				player.statsTotalAssists += 1
				self.statsTotalAssists += 1
				player.passed = 0
	def passerClear(self):
		for player in self.players:
			player.passed = 0
	def seasonStats(self):
		text = "| The {}  --- Rated {} Overall |\n| {} Wins |\n| {} Losses |\n| {:.1f} points per game |\n| {:.1f} rebounds per game |\n| {:.1f} assists per game |\n| {:.1f} steals per game |\n| {:.1f} blocks per game |\n| {:.1f} Turn Overs per game |\n| {:.2f} % Shooting |\n| {:.2f} % Two |\n| {:.2f} % Threes |".format(self.name, self.teamAverage, self.statsWins, self.statsLosses, self.ppg, self.rpg, self.apg, self.spg, self.bpg, self.tpg, self.shotPerc, self.twoTotalPerc, self.threeTotalPerc)
		print(text)
		print("Player Stats:")
		for player in self.players:
			player.seasonStats()
	def reset(self):
		self.statsPoints = 0
		self.statsShots = 0
		self.statsMakes = 0
		self.statsTwos = 0
		self.statsTwosMakes = 0
		self.statsThrees = 0
		self.statsThreesMakes = 0
		self.statsRebounds = 0
		self.statsAssists = 0
		self.statsSteals = 0
		self.statsBlocks = 0
		self.statsTurnOvers = 0
	def newGame(self):
		self.reset()
		for player in self.players:
			player.reset()
	def victory(self):
		for player in self.players:
			player.victory()

	def loss(self):
		for player in self.players:
			player.loss()
	def topPlayer(self):
		players = sorted(self.players, key=lambda player: player.overall, reverse=True)
		return players[0]
	def topScorer(self):
		players = sorted(self.players, key=lambda player: player.ppg, reverse=True)
		return players[0]
	def newSeason(self):
		pass




