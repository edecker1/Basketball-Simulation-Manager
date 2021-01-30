""" 
Game Module
Classesa nd functions related to how the game works
"""
# Import
import random, math
from players import *
# __ GAME CLASS __ #
class Game:
	""" This object will take care of the majority of the functions """
	def __init__(self, teams, limit, ball, message):
		self.teams = teams
		self.limit = limit
		self.ball = ball
		self.message = message
	# ----- Basic Functions ----- #
	def add(self, team):
		self.teams.append(team)
	def remove(self, team):
		self.teams.remove(team)
	def clear(self):
		for team in self.teams:
			self.teams.remove(team)
	# ----- Game Functions ----- #
	def showScores(self):
		""" Shows Scoreboard """
		score1 = self.teams[0].statsPoints
		score2 = self.teams[1].statsPoints
		try:
			name1 = self.teams[0].name
			name2 = self.teams[1].name
		except:
			name1 = self.teams[0].first + " " + self.teams[0].last
			name2 = self.teams[1].first + " " + self.teams[1].last

		print("{} -- {}".format(name1, name2))
		print("{}  --  {}".format(score1, score2))
	def leadScore(self):
		""" Checks lead score to match against winning score """
		score = 0
		for team in self.teams:
			if team.statsPoints > score:
				score = team.statsPoints
		return score
	def start(self):
		try:
			x = self.teams[0].players[0] # see if team
			self.setUp()
		except:
			self.setUp1v1()
	def setUp1v1(self):
		for player in self.teams:
			player.reset()
		firstBall = random.choice(self.teams)
		firstBall.posession = True
	def setUp(self):
		""" Sets up game to start """
		for team in self.teams:
			team.newGame()
		firstBall = random.choice(self.teams)
		ballMan = random.choice(firstBall.players)
		ballMan.posession = True
	def reboundEvent(self, player, enemy, offense, defense):
		""" The event in which soemone gets a rebound """
		offChance = player.rebound * .4
		speedDiff = player.speed - enemy.speed
		heightDiff = (player.height - enemy.height) * 4
		offenseChance = offChance + speedDiff + heightDiff

		chance = random.randint(1, 100)
		if chance > offenseChance:
			enemyRebound = defense.rebounder()
			player.possession = False
			enemyRebound.possession = True
			enemyRebound.statsRebounds += 1
			defense.statsRebounds += 1
			enemyRebound.statsTotalRebounds += 1
			defense.statsTotalRebounds += 1
			return enemyRebound
		else:
			newPlayer = offense.rebounder()
			newPlayer.statsRebounds += 1
			offense.statsRebounds += 1
			newPlayer.statsTotalRebounds += 1
			offense.statsTotalRebounds += 1
			player.possession = False
			newPlayer.possession = True
			return newPlayer
	def rebound1v1(self, player, enemy):
		offChance = player.rebound * .4
		speedDiff = player.speed - enemy.speed
		heightDiff = (player.height - enemy.height) * 4
		offenseChance = offChance + speedDiff + heightDiff

		chance = random.randint(1, 100)
		if chance > offenseChance:
			player.possession = False
			enemy.possession = True
			enemy.statsRebounds += 1
			enemy.statsTotalRebounds += 1
			return enemy
		else:
			player.statsRebounds += 1
			player.statsTotalRebounds += 1
			player.possession = True
			return player
	def victory(self):
		winner = self.teams[0]
		for player in self.teams:
			if player.statsPoints > winner.statsPoints:
				winner = player
			else:
				loser = player
		winner.statsWins += 1
		winner.statsGames += 1
		winner.victory()
		loser.statsLosses += 1
		loser.statsGames += 1
		loser.loss()
		return winner
	def playDuel(self, player, enemy):
		# -- Chance -- #
		chance = random.randint(1, 100)
		# -- Base Limits -- #
		result = 0
		layupLimit = 40
		midLimit = 75
		"""
		Base Chances:
		layup = 40%
		midrange = 35%
		3point = 25%
		"""
		
		# -- Adjust Limits based on skill and cirumstance -- #
		# Set layup limit
		if player.layup > player.midrange:
			layupLimit += random.randint(1, 10)
		else:
			layupLimit -= random.randint(1, 10)
		if player.layup > player.threePoint:
			layupLimit += random.randint(1, 5)
			midLimit += random.randint(1, 5)
		else:
			layupLimit -= random.randint(1, 10)
			midLimit -= random.randint(1, 5)
		# Set mid limit
		if player.midrange > player.threePoint:
			midLimit += random.randint(1,10)
		else:
			midLimit -= random.randint(1,10)
		
		# Adjust for situation
		if player.statsPoints > enemy.statsPoints:
			# More likely to do 2 pointers if ahead
			layupLimit += random.randint(15,25)
			midLimit += random.randint(5, 10)
		else:
			difference = enemy.statsPoints - player.statsPoints
			#if difference huge, more likely to shoot 3s
			midLimit -= (difference * 2)
			layupLimit -= (difference * 2)

		# Street Ball = More threes
		midLimit -= random.randint(1, 10)
		layupLimit -= random.randint(1, 10)
		
		# CHoose the type
		if chance < layupLimit:
			# Layup
			result = player.layupChance(enemy, None)
		elif chance > midLimit:
			# midrange
			result = player.midrangeChance(enemy, None)

		elif chance > midLimit:
			# threepoint
			result = player.threePointChance(enemy, None)

		
		# RESULTS 
		if result == 0:
			# miss = rebound chance
			result = self.rebound1v1(player, enemy)
			print("{} missed and it is rebounded by {}!".format(player.first, result.first))
		elif result == 's':
			# Stolen Ball
			print("Ball stolen by {}".format(enemy.first))
			enemy.posession = True
			player.posession = False
			player.statsTurnOvers += 1
			player.statsTotalTurnOvers += 1
			result = enemy
		elif result > 0:
			# If they Score
			print("{} scores {} points!".format(player.first, result))
			if self.ball == 'winners':
				# IF winners ball, new player on team start with ball
				result = player
			else:
				# If losers ball, defense gets ball
				player.posession = False
				enemy.posession = True
				result = enemy
		return result

	def play(self, player, enemy, offense, defense):
		""" The Player can: Layup, Midrange, Threepoint """
		chance = random.randint(1, 100)
		# -- Base Limits -- #
		result = 0
		layupLimit = 25
		passLimit = 65
		midLimit = 85
		"""
		Base Chances:
		layup = 25%
		pass = 40%
		midrange = 20%
		3point = 15%
		"""

		# -- Adjust Limits based on skill and cirumstance -- #
		# Set layup limit
		if player.layup > player.midrange:
			layupLimit += random.randint(1, 10)
		else:
			passLimit -= random.randint(1, 10)
			midLimit += random.randint(1, 5)
		if player.layup > player.threePoint:
			layupLimit += random.randint(1, 5)
			midLimit += random.randint(1, 10)
		else:
			layupLimit -= random.randint(1, 5)
			midLimit -= random.randint(1, 5)
			passLimit -= random.randint(1, 5)
		# Set mid limit
		if player.midrange > player.threePoint:
			midLimit += random.randint(1,10)
			passLimit -= random.randint(1, 5)
		else:
			midLimit -= random.randint(1,5)
			passLimit -= random.randint(1, 5)

		# Adjust for highest -- Specialty
		if player.layup == player.midrange and player.midrange == player.threePoint and player.midrange == player.passing:
			pass # pass if all equal
		elif player.layup > player.midrange and player.layup > player.threePoint and player.layup > player.passing:
			# if layup is highest
			specialtyDiff = math.ceil(((player.layup - player.midrange) + (player.layup - player.threePoint) + (player.layup - player.passing)) / 3)
			specialtyDiff = specialtyDiff * 2
			layupLimit += random.randint(1, specialtyDiff)
			passLimit += random.randint(1, specialtyDiff)
			midLimit += random.randint(1, specialtyDiff)
		elif player.midrange > player.layup and player.midrange > player.threePoint and player.midrange > player.passing:
			# if midrange is highest
			specialtyDiff = math.ceil(((player.midrange - player.layup) + (player.midrange - player.threePoint) + (player.midrange - player.passing)) / 3)
			specialtyDiff = specialtyDiff * 2
			midLimit += random.randint(1,specialtyDiff)
			layupLimit -= random.randint(1,specialtyDiff)
			passLimit -= random.randint(1, specialtyDiff)
		elif player.threePoint > player.layup and player.threePoint > player.midrange and player.threePoint > player.passing:
			# if 3s are highest
			specialtyDiff = math.ceil(((player.threePoint - player.layup) + (player.threePoint - player.midrange) + (player.threePoint - player.passing)) / 3)
			specialtyDiff = specialtyDiff * 2
			midLimit -= random.randint(1,specialtyDiff)
			passLimit -= random.randint(1, specialtyDiff)
			layupLimit -= random.randint(1,specialtyDiff)
		elif player.passing > player.layup and player.passing > player.midrange and player.passing > player.threePoint:
			# if passing is highest
			specialtyDiff = math.ceil(((player.passing - player.layup) + (player.passing - player.midrange) + (player.passing - player.threePoint)) / 3)
			specialtyDiff = specialtyDiff * 2
			midLimit += random.randint(1,specialtyDiff)
			passLimit += random.randint(1, specialtyDiff)
			layupLimit -= random.randint(1,specialtyDiff)
		else:
			pass # else error

		#Adjust for low ratings
		if player.layup < 70:
			layupLimit -= random.randint(5,10)
			midLimit -= random.randint(1, 5)
			passLimit -= random.randint(1, 5)
		if player.midrange < 70:
			midLimit += random.randint(5,10)
			layupLimit += random.randint(5,10)
			passLimit += random.randint(5, 10)
		if player.threePoint < 70:
			midLimit += random.randint(5,15)
			passLimit += random.randint(1, 5)
			layupLimit += random.randint(1, 5)

		# adjust for opponent 
		if enemy.overall > player.overall:
			passLimit += random.randint(5,15)
			layupLimit -= random.randint(5,15)
			midLimit += random.randint(1, 5)
		else:
			pass

		# Adjust for situation
		if offense.statsPoints > defense.statsPoints:
			# More likely to do 2 pointers if ahead
			layupLimit += random.randint(15,25)
			midLimit += random.randint(5, 10)
		else:
			difference = defense.statsPoints - offense.statsPoints
			#if difference huge, more likely to shoot 3s
			midLimit -= (difference * 2)
			passLimit -= (difference * 2)
			layupLimit -= (difference * 2)


		# Adjust for amount of shots taken
		try:
			shotBalance = math.ceil((player.statsShots / offense.statsShots) * 100)
			if shotBalance > 80 and player.statsShots > 10:
				layupLimit -= random.randint(10, 15)
				passLimit += random.randint(20, 25)
				midLimit += 15
			elif shotBalance < 20:
				passLimit -= 20
				midLimit -= 5
				layupLimit += 20
		except:
			pass

		# For no erros, fix limits if gone wacky
		if layupLimit > passLimit:
			passLimit = layupLimit + 1
		if passLimit > midLimit:
			midLimit = passLimit + 1

		# Street Ball = More threes
		midLimit -= random.randint(1, 10)
		passLimit -= random.randint(1, 10)

		# CHoose the type
		if chance < layupLimit:
			# Layup
			result = player.layupChance(enemy, defense)
			offense.statsShots += 1
			offense.statsTwos += 1
			offense.statsTotalShots += 1
			offense.statsTotalTwos += 1
		elif chance > layupLimit and chance < passLimit:
			# pass
			result = player.passChance(offense, enemy)
			passed = 1
		elif chance > passLimit and chance < midLimit:
			# midrange
			result = player.midrangeChance(enemy, defense)
			offense.statsShots += 1
			offense.statsTwos += 1
			offense.statsTotalShots += 1
			offense.statsTotalTwos += 1
		elif chance > midLimit:
			# threepoint
			result = player.threePointChance(enemy, defense)
			offense.statsShots += 1
			offense.statsThrees += 1
			offense.statsTotalShots += 1
			offense.statsTotalThrees += 1
		
		# RESULTS 
		if isinstance(result, Player):
			# Pass
			result.posession = True
			player.posession = False
		elif result == 0:
			# miss = rebound chance
			result = self.reboundEvent(player, enemy, offense, defense)
			offense.passerClear()
		elif result == 's':
			# Stolen Ball
			enemy.posession = True
			player.posession = False
			defense.statsSteals += 1
			offense.statsTurnOvers += 1
			player.statsTurnOvers += 1
			defense.statsTotalSteals += 1
			offense.statsTotalTurnOvers += 1
			player.statsTotalTurnOvers += 1
			result = enemy
			offense.passerClear()
		elif result == 't':
			# TIPPED BALL
			stolen = defense.chooseBallHandler()
			stolen.statsSteals += 1
			defense.statsSteals += 1
			offense.statsTurnOvers += 1
			stolen.statsTotalSteals += 1
			defense.statsTotalSteals += 1
			offense.statsTotalTurnOvers += 1
			result = stolen
			offense.passerClear()
		elif result > 0:
			# If they Score
			offense.statsPoints += result
			offense.statsMakes += 1
			offense.statsTotalPoints += result
			offense.statsTotalMakes += 1
			# assist check 
			offense.passerCheck()
			if result == 2:
				offense.statsTwosMakes += 1
				offense.statsTotalTwosMakes += 1
			else:
				offense.statsThreesMakes += 1
				offense.statsTotalThreesMakes += 1
			if self.ball == 'winners':
				# IF winners ball, new player on team start with ball
				player.posession = False
				newBallHandler = offense.chooseBallHandler()
				result = newBallHandler
			else:
				# If losers ball, defense gets ball
				player.posession = False
				newBallHandler = defense.chooseBallHandler()
				result = newBallHandler
		return result
	def findOffense(self):
		o = None
		try:
			for team in self.teams:
				check = team.checkPosession()
				if check is True:
					o = team
		except:
			for player in self.teams:
				if player.posession is True:
					o = player
		return o
	def findDefense(self, offense):
		d = None
		try:
			for team in self.teams:
				if team.name != offense.name:
					d = team
		except:
			for player in self.teams:
				if player.posession is False:
					d = player
		return d
	def findBallHandler(self, team):
		try:
			for player in team.players:
				if player.posession == True:
					return player
		except:
			return team
	def findGuard(self, team):
		try:
			player = random.choice(team.players)
			return player
		except:
			return team
	def exhibition(self):
		""" Main Game Function """
		self.start()
		score = 0
		while score < self.limit:
			offense = self.findOffense()
			defense = self.findDefense(offense)
			ballHandler = self.findBallHandler(offense)
			guard = self.findGuard(defense)
			action = self.play(ballHandler, guard, offense, defense)
			ballHandler.posession = False
			action.posession = True
			score = self.leadScore()
		winner = self.victory()
		if self.message is True:
			self.showScores()
		return winner
	def duel(self):
		""" 1 v1 Game """
		self.start()
		score = 0
		while score < self.limit:
			offense = self.findOffense()
			defense = self.findDefense(offense)
			result = self.playDuel(offense, defense)
			if result is offense:
				pass
			else:
				offense.posession = False
				defense.posession = True
			score = self.leadScore()
			self.showScores()
		winner = self.victory()
		if self.message is True:
			self.showScores()
		return winner
	def playGame(self):
		try:
			# see if its a team
			x = self.teams[0].players[0]
			result = self.exhibition()
		except:
			result = self.duel()


		return result

