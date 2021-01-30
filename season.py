""" Season FIle
1) Season should take in the teams, numberofGames
2) Make conferences by splitting team in half
3) Maybe minimum of two teams?
4) Then create a randomized schedule of the other teams
5) Then simulate season
6) Playoffs - Basically watered down version of tournament code
7) championship
8) End of Seasons awards
9) Maybe a season stats ranking?
10) Menu - Simulate, viewStats, etc... go game by game?
"""
import random
import math
from tabulate import tabulate
from game import *
from teams import *

class Season:
	teamCities = ['Worcester', 'Fitchburg', 'Lowell', 'Auburn', 'Shrewsbury', 'Framingham', 'Wrentham', 'Nashua', 'Boston', 'Dorchester', 'Leominster', 'Westborough', 'Northborough', 'West Boyleston']
	teamNames = ['Patriots', 'Militia', 'Fish', 'Sharks', 'Turtles', 'Gunslingers', 'Ghosts', 'Assasins', 'Outlaws', 'Rhinos', 'Stars', 'Moons', 'Knights', 'Crusaders', 'Shinobi', 'Kage', 'Ninja']
	logger = []
	conference1 = []
	conference2 = []
	champion = ''
	mvp = ''

	def __init__(self, teams):
		self.teams = teams
	def setNames(self):
		for team in self.teams:
			name1 = random.choice(self.teamCities)
			name2 = random.choice(self.teamNames)
			self.teamCities.remove(name1)
			self.teamNames.remove(name2)
			name3 = name1 + ' ' + name2
			team.name = name3
	def addBack(self):
		for team in self.conference1:
			self.teams.append(team)
		for team in self.conference2:
			self.teams.append(team)
	def setConferences(self):
		half = len(self.teams) / 2
		# Set conference 1
		while len(self.conference1) != half:
			team = random.choice(self.teams)
			self.conference1.append(team)
			self.teams.remove(team)
		# Set conference 2
		while len(self.conference2) != half:
			for team in self.teams:
				self.conference2.append(team)
				self.teams.remove(team)
		# add back to self.teams
		self.addBack()

		print("Conferences have been set")
	def printConferences(self):
		print("\n -- || The East Conference || --")
		x = 1
		for team in self.conference1:
			print(" {}. || The {} || ".format(x, team.name))
			print("    Rated -- {} ---".format(team.teamAverage))
			print("     {}".format(team.topPlayer()))
			x += 1
		x = 1
		print("\n -- || The West Conference || --")
		for team in self.conference2:
			print(" {}. || The {} || ".format(x, team.name))
			print("    Rated -- {} ---".format(team.teamAverage))
			print("     {}".format(team.topPlayer()))
			x += 1
	def setSchedule(self):
		# create schedule for each team
		# Play outside conference twice
		# Play conference Four?
		conferenceLength = len(self.conference1)
		numOfGames = ((conferenceLength - 1) * 4) + (conferenceLength * 2)
		print("{} is the number of games each team will play".format(numOfGames))
		index = 0
		# Set conference 1 -- Needs tyo be reworked to condense eventually
		while index < len(self.conference1):
			schedule = []
			for team in self.conference1:
				if team is self.conference1[index]:
					pass
				else:
					schedule.append(team.name)
					schedule.append(team.name)
					schedule.append(team.name)
					schedule.append(team.name)
			for team in self.conference2:
				schedule.append(team.name)
				schedule.append(team.name)

			self.conference1[index].schedule = schedule
			index += 1

		index = 0
		# set conference 2
		while index < len(self.conference2):
			schedule = []
			for team in self.conference2:
				if team is self.conference2[index]:
					pass
				else:
					schedule.append(team.name)
					schedule.append(team.name)
					schedule.append(team.name)
					schedule.append(team.name)
			for team in self.conference1:
				schedule.append(team.name)
				schedule.append(team.name)

			self.conference2[index].schedule = schedule
			index += 1
		print("Schedules complete")
	def printSchedule(self, team):
		print("-------------------------------------------------")
		print("{}'s schedule for the upcoming season:".format(team.name))
		print("-------------------------------------------------")
		x = 1
		for game in team.schedule:
			print("{}. {}".format(x, game))
			x += 1
	def printAllSchedules(self):
		for team in self.teams:
			print("-------------------------------------------------")
			print("{}'s schedule for the upcoming season:".format(team.name))
			print("-------------------------------------------------")
			x = 1
			if not team.schedule:
				print("ERROR! NO SCHEDULE")
			else:
				for game in team.schedule:
					print("{}. {}".format(x, game))
					x += 1
	def setup(self):
		if isinstance(self.teams[0], Team):
			self.setNames()
			self.setConferences()
			self.printConferences()
			self.setSchedule()
			print("Season ready to commence")
		else:
			# If players are put into season
			newTeams = []
			for team in self.teams:
				text = team.first + " " + team.last
				temp = Team([team], text)
				newTeams.append(temp)
			self.teams.clear()
			for team in newTeams:
				self.teams.append(team)
			self.setConferences()
			self.printConferences()
			self.setSchedule()
			print("Season ready to commence")

	def log(self, text):
		self.logger.append(text)
	def showLog(self):
		x = 1
		for logging in self.logger:
			print("{}. {}".format(x, logging))
			x += 1
	def leadingScorer(self):
		lead = 0
		topScorer = ''
		for team in self.teams:
			top = team.topScorer()
			if top.ppg > lead:
				lead = top.ppg
				topScorer = top
		weekScorer = "{} {} is the leagues leading scorer with {} points per game!".format(topScorer.first, topScorer.last, topScorer.ppg)
		self.log(weekScorer)
	def checkGamesPlayed(self):
		left = []
		flag = 0
		for team in self.teams:
			left.append((len(team.schedule)))
		first = left[0]
		for item in left:
			if item != first:
				flag = 1
		if flag == 0:
			return True
		else:
			return False 
	def oneWeek(self, weekNumber):
		gamesLeft = len(self.teams[0].schedule) # This is how many games each team should have left
		weekBeginning = ' --- Week {} --- '.format(weekNumber)
		print("{} games left for each team".format(gamesLeft))
		self.log(weekBeginning)
		for team in self.teams:
			# find teams
			if len(team.schedule) < gamesLeft: 
				pass # if already played
			elif not team.schedule:
				pass # If done with schedule
			else:
				flag = 1 # Flag for when proper opponent is picked
				x = 0
				while flag != 0:
					name = random.choice(team.schedule)
					for player in self.teams:
						if player.name == name:
							team1 = player # set the opponent team
					if len(team1.schedule) == gamesLeft:
						flag = 0
					else:
						x += 1
						#print("{} times searching for opponent".format(x))
						if x > 30:
							flag = 0
							print("{} has to play twice this week!".format(team1.name))
						else:
							pass # Team already played
				# Simulate Game
				game = Game([team, team1], 21, 'winners', False)
				winner = game.exhibition()
				if winner is team:
					text = "{} beat {} with the score being: {} - {}".format(team.name, team1.name, team.statsPoints, team1.statsPoints)
					self.log(text)
				else:
					text = "{} beat {} with the score being: {} - {}".format(team1.name, team.name, team1.statsPoints, team.statsPoints)
				team.schedule.remove(team1.name)
				team1.schedule.remove(team.name)
		self.leadingScorer()
	def printTeams(self):
		x = 1
		for team in self.teams:
			print("{}. {}".format(x, team.name))
			x += 1
	def simulate(self):
		""" Simulates a whole season """
		counter = 1
		week = 1
		while counter != 0:
			self.oneWeek(week)
			week += 1
			counter = len(self.teams[0].schedule)
	def seasonMode(self):
		self.setup()
		self.simulate()
		self.teamRanking()
		self.playerRankings('points')
		self.mvp()
	def playerSeasonRanked(self):
		print("--Player Season Stats--")
		players = []
		for team in self.teams:
			for player in team.players:
				players.append(player)

		ranked = sorted(players, key=lambda player: player.ppg, reverse=True)
		x = 1
		for player in ranked:
			print(" ----- || Rank {} || -----".format(x))
			player.seasonStats()
			x += 1
	def playerRankings(self, attribute):
		print("\n\n")
		players = []
		for team in self.teams:
			for player in team.players:
				players.append(player)
		if attribute == 'points':
			print(" ----- || Player Point Rankings || -----")
			print("")
			ranked = sorted(players, key=lambda player: player.ppg, reverse=True)
			table = [['Rank', 'Name', 'PPG', 'Shot Percentage', 'Total Makes', 'Total Attempts']]
			x = 1
			for player in ranked:
				rank = "{}.".format(x)
				name = "{} {}".format(player.first, player.last)
				ppg = round(player.ppg, 1)
				makes = player.statsTotalMakes
				attempts = player.statsTotalShots
				try:
					raw = (makes / attempts) * 100
				except:
					raw = 0
				perc = round(raw, 1)
				final = "{} %".format(perc)
				add = [rank, name, ppg, final, makes, attempts]
				table.append(add)
				x += 1
			print(tabulate(table, headers="firstrow"))
		elif attribute == 'assists':
			print(" ----- || Player Assist Rankings || -----")
			print("")
			ranked = sorted(players, key=lambda player: player.apg, reverse=True)
			table = [['Rank', 'Name', 'APG', 'Total Assists']]
			x = 1
			for player in ranked:
				rank = "{}.".format(x)
				name = "{} {}".format(x, player.first, player.last)
				apg = round(player.apg, 1)
				total = player.statsTotalAssists
				add = [rank, name, apg, total]
				table.append(add)
				x += 1
			print(tabulate(table, headers="firstrow"))
		elif attribute == 'rebounds':
			print(" ----- || Player Rebound Rankings || -----")
			print("")
			ranked = sorted(players, key=lambda player: player.rpg, reverse=True)
			table = [['Rank', 'Name', 'RPG', 'Total Rebounds']]
			x = 1
			for player in ranked:
				rank = "{}.".format(x)
				name = "{} {}".format(x, player.first, player.last)
				rpg = round(player.rpg, 1)
				total = player.statsTotalRebounds
				add = [rank, name, rpg, total]
				table.append(add)
				x += 1
			print(tabulate(table, headers="firstrow"))
		elif attribute == 'steals':
			print(" ----- || Player Steals Rankings || -----")
			print("")
			ranked = sorted(players, key=lambda player: player.spg, reverse=True)
			table = [['Rank','Name', 'SPG', 'Total Steals']]
			x = 1
			for player in ranked:
				rank = "{}.".format(x)
				name = "{} {}".format(x, player.first, player.last)
				spg = round(player.spg, 1)
				total = player.statsTotalSteals
				add = [rank, name, spg, total]
				table.append(add)
				x += 1
			print(tabulate(table, headers="firstrow"))
		elif attribute == 'blocks':
			print(" ----- || Player Blocks Rankings || -----")
			print("")
			ranked = sorted(players, key=lambda player: player.bpg, reverse=True)
			table = [['Rank','Name', 'BPG', 'Total Blocks']]
			x = 1
			for player in ranked:
				rank = "{}.".format(x)
				name = "{} {}".format(x, player.first, player.last)
				bpg = round(player.bpg, 1)
				total = player.statsTotalBlocks
				add = [rank, name, bpg, total]
				table.append(add)
				x += 1
			print(tabulate(table, headers="firstrow"))
		elif attribute == 'threes':
			print(" ----- || Player 3-Point Rankings || -----")
			print("")
			ranked = sorted(players, key=lambda player: player.threeTotalPerc, reverse=True)
			table = [['Rank', 'Name', 'Three Point %', 'Threes Made', 'Threes Attempted', 'Point % from Threes']]
			x = 1
			for player in ranked:
				rank = "{}.".format(x)
				name = "{} {}".format(x, player.first, player.last)
				threes = round(player.threeTotalPerc, 1)
				total = player.statsTotalThrees
				makes = player.statsTotalThreesMakes
				rawThree = player.statsTotalThreesMakes * 3
				raw = (rawThree / player.statsTotalPoints) * 100
				perc = round(raw, 2)
				final = "{} %".format(perc)
				add = [rank, name, threes, makes, total, final]
				table.append(add)
				x += 1
			print(tabulate(table, headers="firstrow"))
		else:
			print("ERROR")
	def teamRanking(self):
		ranked = sorted(self.teams, key=lambda team: team.statsWins, reverse=True)
		table = [['Rank',"Team Name", "Wins", "Losses", "Win Percentage"]]
		x = 1
		for team in ranked:
			rank = "{}.".format(x)
			name = "{}".format(team.name)
			win = team.statsWins
			loss = team.statsLosses
			try:
				raw = (team.statsWins / team.statsGames) * 100
			except:
				raw = 0
			perc = round(raw, 1)
			final = "{} %".format(perc)
			add = [rank, name, win, loss, final]
			table.append(add)
			x += 1

		print(" -- Team Rankings --")
		print(tabulate(table, headers="firstrow"))
	def mvp(self):
		players = []
		top = []
		# Get players together and clear mvp rating
		for team in self.teams:
			for player in team.players:
				players.append(player)
				player.mvp = 0
		# Get MVP total
		for player in players:
			totalPoints = math.ceil( (player.statsTotalPoints * .6) + (player.statsTotalRebounds * .10) + (player.statsTotalAssists * .15) + (player.statsTotalSteals * .10) + (player.statsTotalBlocks * .05) )
			player.mvp = totalPoints
			print("{} has {} MVP Points".format(player.first, totalPoints))
		# Order
		ranked = sorted(players, key=lambda player: player.mvp, reverse=True)
		top.append(ranked[0])
		top.append(ranked[1])
		top.append(ranked[2])
		for player in top:
			print("{} {} ".format(player.first, player.last))
		print("{} {} is the league's MVP!".format(top[0].first, top[0].last))
		table = [["Rank", "Name", "PPG", "APG", "RPG", "SPG", "BPG", "Shot Percentage", "Three Percentage"]]
		x = 1
		for player in top:
			rank = x
			name = "{} {}".format(player.first, player.last)
			ppg = "{}".format(round(player.ppg, 1))
			apg = "{}".format(round(player.apg, 1))
			rpg = "{}".format(round(player.rpg, 1))
			spg = "{}".format(round(player.spg, 1))
			bpg = "{}".format(round(player.bpg, 1))
			shots = "{}%".format(round(player.shotPerc, 1))
			threes = "{}%".format(round(player.threeTotalPerc, 1))
			table.append([rank, name, ppg, apg, rpg, spg, bpg, shots, threes])
			x += 1
		print(tabulate(table, headers="firstrow"))














class Menu:
	def __init__(self, team, season):
		self.team = team
	def seasonMenu(self):
		print("--Welcome to your season mode!--")
		print(" - You are following {}!".format(self.team))
		print("\nWhat would you like to do?")
		print("1. Simulate One Week")
		print("2. Simulate Season")
		print("3. View Team")
		print("4. View Team Ranking")
		print("5. View Player Ranking")
		choice = int(input(">>  "))
		try:
			if choice == 1:
				season.oneWeek()
			elif choice == 2:
				season.seasonMode()
			elif choice == 3:
				self.team.seasonStats()
			elif choice == 4:
				season.TeamRanking()
			elif choice == 5:
				self.playerRankings('point')
		except:
			print("ERROR")
