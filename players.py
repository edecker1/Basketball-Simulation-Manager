"""
This module will hold all information related to players
will have the player class
"""
import math, random
from stats import *
class Player(Stats):
	""" Player objects
	 """


	# Game Variables
	posession = False
	passed = 0
	energy = 100
	# Season Variables
	mvp = 0

	def __init__(self, first, last, height, speed, agility, endurance, passing, layup, midrange, threePoint, steal, defense, rebound):
		# Name Variables
		self.first = first
		self.last = last
		# Height in Inches
		self.height = height
		# Athletics 1 - 100
		self.speed = speed
		self.agility = agility
		self.endurance = endurance 
		# Skills 1 - 100
		self.passing = passing
		self.layup = layup
		self.midrange = midrange
		self.threePoint = threePoint
		self.steal = steal
		self.defense = defense
		self.rebound = rebound
	@property
	def overall(self):
		# Overall based on Skills
		self._overall = math.ceil(((self.layup + self.midrange + self.threePoint + self.steal + self.defense + self.rebound) / 600) * 100)
		return self._overall
	def __repr__(self):
		text = "{} {}: {}".format(self.first, self.last, self.overall)
		return text
	def luckModifier(self):
		# Luck Modifier for shots
		x = random.randint(1, 2)
		if x == 1:
			y = random.randint(5, 10)
		else:
			y = -(random.randint(5, 10))
		return y
	def exhaustionCheck(self):
		check = 10
		check -= (self.endurance * .1)
		self.energy -= check
	def energyModifier(self):
		if self.energy > 90:
			return 0
		elif self.energy > 50 and self.energy < 90:
			modifier = random.randint(1, 5)
			return modifier
		elif self.energy > 25 and self.energy < 50:
			modifier = random.randint(4, 8)
			return modifier
		elif self.energy > 0 and self.energy < 25:
			modifier = random.randint(6, 11)
			return modifier
		elif self.energy < 0:
			modifier = random.randint(8, 14)
			return modifier
		else:
			return 0
	def layupChance(self, enemy, team):
		self.statsShots += 1
		self.statsTwos += 1
		self.statsTotalShots += 1
		self.statsTotalTwos += 1
		self.exhaustionCheck()
		baseChance = 5
		skill = math.ceil(self.layup * .55)
		defendingChance = math.ceil(enemy.defense * .2)
		defenseTwo = math.ceil(enemy.steal * .1)
		speedDiff = (self.speed - enemy.speed) 
		agilityDiff = (self.agility - enemy.agility)
		heightDiff = math.ceil((self.height - enemy.height) * 1.5)

		total = baseChance + skill + speedDiff + agilityDiff - defendingChance - defenseTwo + int(self.luckModifier()) + heightDiff - int(self.energyModifier())
		chance = random.randint(1, 100)
		if chance > total:
			if total < 10:
				enemy.statsBlocks += 1
				enemy.statsTotalBlocks += 1
				if team is None:
					pass
				else:
					team.statsBlocks += 1
					team.statsTotalBlocks += 1
				return 0
			else:
				return 0
		else:
			self.statsTwosMakes += 1
			self.statsMakes += 1
			self.statsPoints += 2
			self.statsTotalTwosMakes += 1
			self.statsTotalMakes += 1
			self.statsTotalPoints += 2
			self.energy += 1
			return 2
	def midrangeChance(self, enemy, team):
		self.statsShots += 1
		self.statsTwos += 1
		self.statsTotalShots += 1
		self.statsTotalTwos += 1
		self.exhaustionCheck()
		baseChance = 5
		skill = math.ceil(self.midrange * .45)
		defendingChance = math.ceil(enemy.defense * .2)
		speedDiff = self.speed - enemy.speed
		agilityDiff = self.agility - enemy.agility

		total = baseChance + skill + speedDiff + agilityDiff - defendingChance + int(self.luckModifier()) - int(self.energyModifier())
		chance = random.randint(1, 100)
		if chance > total:
			if total < 7:
				enemy.statsBlocks += 1
				enemy.statsTotalBlocks += 1
				if team is None:
					pass
				else:
					team.statsTotalBlocks += 1
					team.statsBlocks += 1
				return 0
			else:
				return 0
		else:
			self.statsTwosMakes += 1
			self.statsMakes += 1
			self.statsPoints += 2
			self.statsTotalTwosMakes += 1
			self.statsTotalMakes += 1
			self.statsTotalPoints += 2
			self.energy += 1
			return 2
	def threePointChance(self, enemy, team):
		self.statsShots += 1
		self.statsThrees += 1
		self.statsTotalShots += 1
		self.statsTotalThrees += 1
		self.exhaustionCheck()
		skill = math.ceil(self.threePoint * .4)
		defendingChance = math.ceil(enemy.defense * .1)

		total = skill - defendingChance + int(self.luckModifier()) - int(self.energyModifier())
		chance = random.randint(1, 100) 
		if chance > total:
			if total < 5:
				enemy.statsBlocks += 1
				enemy.statsTotalBlocks += 1
				if team is None:
					pass
				else:
					team.statsTotalBlocks += 1
					team.statsBlocks += 1
				return 0
			else:
				return 0
		else:
			self.statsThreesMakes += 1
			self.statsMakes += 1
			self.statsPoints += 3
			self.statsTotalThreesMakes += 1
			self.statsTotalMakes += 1
			self.statsTotalPoints += 3
			self.energy += 1
			return 3
	def passChance(self, team, enemy):
		# Make sure target isn't self
		self.energy += 2
		target = random.choice(team.players)
		if target is self:
			while target is self:
				target = random.choice(team.players)
		# Steal Check
		steal = enemy.stealChance(self)
		if steal == False:
			self.possession = False
			# Pass check
			chance = random.randint(1, 100)
			total = self.passing - math.ceil(enemy.defense * random.random())
			if chance > total:
				target.possession = True
				self.passed = 1
				return target
			else:
				self.statsTurnOvers += 1
				self.statsTotalTurnOvers += 1
				return 't'
		else:
			# Stolen
			return 's'
	def stealChance(self, enemy):
		self.exhaustionCheck()
		baseChance = self.steal * .2
		speedDiff = self.speed - enemy.speed
		defenseSkill = (enemy.defense * .1)
		total = baseChance + speedDiff + defenseSkill
		chance = random.randint(1, 100)
		if chance > total:
			return False
		else:
			self.statsSteals += 1
			self.statsTotalSteals += 1
			return True
	def seasonStats(self):
		text = "| {} {} --- Rated {} Overall |\n| {:.1f} points per game |\n| {:.1f} rebounds per game |\n| {:.1f} assists per game |\n| {:.1f} steals per game |\n| {:.1f} blocks per game |\n| {:.1f} Turn Overs per game |\n| {:.2f} % Shooting |\n| {:.2f} % Two |\n| {:.2f} % Threes |".format(self.first, self.last, self.overall, self.ppg, self.rpg, self.apg, self.spg, self.bpg, self.tpg, self.shotPerc, self.twoTotalPerc, self.threeTotalPerc)
		print(text)
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
		self.energy = 100
	def showStats(self):
		print("|| {} {} -- {} Overall ||".format(self.first, self.last, self.overall))
		self.statLine()
	def victory(self):
		self.statsGames += 1
		self.statsWins += 1
	def loss(self):
		self.statsGames += 1
		self.statsLosses +=1
