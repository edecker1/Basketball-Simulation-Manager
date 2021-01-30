"""
This will be the Stats classs to clean up the Player and Team classes
Thsi way all stats can be done here
"""

import random
import math

class Stats:
	# Career Stats
	statsCareerMVP = 0
	statsCareerSeasons = 0
	statsCareerGames = 0
	statsCareerWins = 0
	statsCareerLosses = 0
	statsCareerShots = 0
	statsCareerMakes = 0
	statsCareerPoints = 0
	statsCareerTwos = 0
	statsCareerTwosMakes = 0
	statsCareerThrees = 0
	statsCareerThreesMakes = 0
	statsCareerRebounds = 0
	statsCareerAssists = 0
	statsCareerSteals = 0
	statsCareerBlocks = 0
	statsCareerTurnOvers = 0
	# Season Stats
	statsGames = 0
	statsWins = 0
	statsLosses = 0
	statsTotalShots = 0
	statsTotalMakes = 0
	statsTotalPoints = 0
	statsTotalTwos = 0
	statsTotalTwosMakes = 0
	statsTotalThrees = 0
	statsTotalThreesMakes = 0
	statsTotalRebounds = 0
	statsTotalAssists = 0
	statsTotalSteals = 0
	statsTotalBlocks = 0
	statsTotalTurnOvers = 0
	 # Game Stats
	statsPoints = 0
	statsShots = 0
	statsMakes = 0
	statsTwos = 0
	statsTwosMakes = 0
	statsThrees = 0
	statsThreesMakes = 0
	statsRebounds = 0
	statsAssists = 0
	statsSteals = 0
	statsBlocks = 0
	statsTurnOvers = 0
	@property
	def ppg(self):
		try:
			self._ppg = (self.statsTotalPoints / self.statsGames)
		except:
			self._ppg = 0

		return self._ppg
	@property
	def bpg(self):
		try:
			self._ppg = (self.statsTotalBlocks / self.statsGames)
		except:
			self._ppg = 0

		return self._ppg
	@property
	def apg(self):
		try:
			self._apg = (self.statsTotalAssists / self.statsGames)
		except:
			self._apg = 0
		return self._apg
	@property
	def rpg(self):
		try:
			self._rpg = (self.statsTotalRebounds / self.statsGames)
		except:
			self._rpg = 0
		return self._rpg
	@property
	def spg(self):
		try:
			self._spg = (self.statsTotalSteals / self.statsGames)
		except:
			self._spg = 0
		return self._spg
	@property
	def tpg(self):
		try:
			self._tpg = (self.statsTotalTurnOvers / self.statsGames)
		except:
			self._tpg = 0
		return self._tpg
	@property
	def shotPerc(self):
		try:
			self._sPerc = ((self.statsTotalMakes / self.statsTotalShots) * 100)
		except:
			self._sPerc = 0
		return self._sPerc
	@property
	def twoTotalPerc(self):
		try:
			self._tPerc = ((self.statsTotalTwosMakes / self.statsTotalTwos) * 100)
		except:
			self._tPerc = 0
		return self._tPerc
	@property
	def threeTotalPerc(self):
		try:
			self._tPerc = ((self.statsTotalThreesMakes / self.statsTotalThrees) * 100)
		except:
			self._tPerc = 0
		return self._tPerc
	@property
	def twoPerc(self):
		# Two Point Percentage
		try:
			self._twoPerc = math.ceil(((self.statsTwosMakes / self.statsTwos) * 100))
		except:
			self._twoPerc = 0 # In case of no shots
		return self._twoPerc
	@property
	def threePerc(self):
		try:
			self._threePerc = math.ceil(((self.statsThreesMakes / self.statsThrees) * 100))
		except:
			self._threePerc = 0 # In case of no shots
		return self._threePerc
	@property
	def totalPerc(self):
		try:
			self._totalPerc = math.ceil(((self.statsMakes / self.statsShots) * 100))
		except:
			self._totalPerc = 0 # In case of no shots
			print("{} is makes and {} is shots ".format(self.statsMakes, self.statsShots))
		return self._totalPerc
	def statLine(self):
		# For games
		text = "{} Points\n{} / {} Shots -- {}%\n{} / {} Twos -- {}%\n{} / {} Threes -- {}%\n{} Rebounds \n{} Steals\n{} Assists\n{} Blocks\n{} Turn Overs".format(self.statsPoints, self.statsMakes, self.statsShots, self.totalPerc, self.statsTwosMakes, self.statsTwos, self.twoPerc, self.statsThreesMakes, self.statsThrees, self.threePerc, self.statsRebounds, self.statsSteals, self.statsAssists, self.statsBlocks, self.statsTurnOvers)
		print(text)

