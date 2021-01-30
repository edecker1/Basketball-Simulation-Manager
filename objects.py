"""
This will have all of the objects for the game
"""
import math, random
from game import *
from players import *
from teams import *
from tournament import *
from season import *


# Player: first, last, height, speed, agility, endurance, passing, layup, midrange, threePoint, steal, defense, rebound #
               # Name,   Name     HEI SPD AGI END PAS LAY MID THRE STE DEF REB
# Wack
sharon = Player('Sharon', 'Del Valle', 63, 85, 85, 95, 75, 70, 70 ,70, 80, 85, 75)
caroline = Player('Caroline', 'Anderson', 66, 75, 75, 80, 75, 80, 70, 65, 79, 82, 82)
melanie = Player('Melanie', 'Del Valle', 63, 85, 85, 75, 75, 70, 70 ,70, 75, 80, 70)
kat2 = Player('Kat', 'Evasius', 64, 60, 62, 100, 75, 65, 70, 65, 90, 95, 70)
krystal = Player('Krystal', 'Thorpe', 68, 90, 90, 85, 70, 60, 60, 45, 95, 90, 65)
becca = Player('Becca', 'Patterson', 63, 70, 70, 70, 75, 70, 75, 75, 70, 70, 70)
kat = Player('Kat', 'Pellerin', 65, 75, 75, 85, 75, 75, 85, 75, 75, 80, 75)
manny = Player('Manny', 'Marrero', 71, 86, 89, 95, 85, 85, 80, 75, 75, 83, 88)
omar = Player('Omar', 'Cordova', 67, 92, 88, 99, 82, 79, 50, 70, 95, 90, 99)
rodney = Player('Rodney', 'Agare-May', 71, 98, 99, 99, 90, 90, 95, 80, 75, 75, 90)
stephon = Player('Stephon', 'Rosario', 70, 80, 88, 90, 90, 85, 70, 80, 70, 75, 85)
jon = Player('Jon', 'Cruz', 68, 83, 86, 85, 95, 85, 80, 85, 75, 85, 75)
ethan = Player('Ethan', 'Decker', 70, 88, 85, 70, 85, 72, 78, 84, 80, 83, 72)
nhan = Player('Nhan', 'Le', 68, 85, 90, 90, 90, 70, 65, 90, 95, 90, 80)
timmy = Player('Timmy', 'Wu', 71, 75, 75, 85, 80, 65, 65, 80, 85, 85, 70)
jake = Player('Jake', 'Fontanez', 69, 80, 84, 75, 80, 85, 70, 80, 70, 70, 70)
jimmy = Player('Jimmy', 'Strong', 75, 80, 75, 80, 75, 83, 75, 90, 75, 75, 75)
andrew = Player('Andrew', 'Persson', 63, 75, 78, 75, 85, 70, 79, 83, 75, 75, 70)
tyler = Player('Tyler', 'Sennick', 73, 95, 80, 100, 70, 15, 10, 5, 95, 95, 95)
trevor = Player('Trevor', 'Sennick', 76, 82, 80, 70, 70, 70, 70, 70, 70, 70, 70)
yanis = Player('Tyler', 'Yanis', 71, 80, 80, 80, 75, 80, 75, 72, 80, 85, 85)
cameron = Player('Cameron', 'Leblanc', 67, 88, 88, 95, 75, 70, 70, 70, 85, 85, 75)
jeff = Player('Jeff', 'Persson', 67, 85, 80, 85, 80, 75, 75, 85, 85, 80, 80)
alex = Player('Alex', 'Costa', 70, 80, 75, 75, 75, 55, 60, 55, 80, 90, 80)
# Anime
kagami = Player("Taiga", "Kagami", 75, 85, 85, 90, 80, 98, 85, 70, 75, 80, 99)
kuroko = Player("Tetsuya", "Kuroko", 66, 70, 70, 70, 100, 60, 80, 50, 95, 70, 45)
midorima = Player("Shintaro", "Midorima", 77, 80, 80, 95, 80, 85, 90, 100, 80, 85, 80)
aomine = Player("Daiki", "Aomine", 76, 100, 100, 100, 50, 90, 90, 90, 85, 85, 75)
murasakibara = Player("Atsushi", "Murasakibara", 82, 75, 85, 70, 70, 99, 70, 70, 75, 99, 99)
kise = Player("Ryota", "Kise", 74, 85, 85, 85, 85, 85, 85, 85, 85, 85, 85)

animeTeam = Team('Vorpal Swords', [midorima, aomine, murasakibara, kise, kuroko])
kageTeam = Team('The Kage', [ethan, omar, nhan, timmy, stephon])

roster = [sharon, caroline, melanie, kat2, krystal, becca, kat, manny, omar, rodney, stephon, jon, ethan, nhan, timmy, jake, jimmy, andrew, tyler, trevor, yanis, cameron, jeff, alex, kagami, kuroko, midorima, aomine, murasakibara, kise]

# Teams , name, players
# 3 v 3 Teams
threeTeam1 = Team('Fitchburg', [sharon, caroline, melanie])
threeTeam2 = Team("The Duelists", [kat, manny, omar])
threeTeam3 = Team("Good Players", [rodney, stephon, jon])
threeTeam4 = Team("Kage", [ethan, nhan, timmy])
threeTeam5 = Team("Jake Squad", [jake, jimmy, andrew])
threeTeam6 = Team('Girls', [kat2, krystal, becca])
threeTeam7 = Team('Dungeons and Dragons', [tyler, trevor, yanis])
threeTeam8 = Team('The Exiled', [cameron, jeff, alex])
teamsThrees = [threeTeam1, threeTeam2, threeTeam3, threeTeam4, threeTeam5, threeTeam6, threeTeam7, threeTeam8]
# 2v2 Teams
twoTeam1 = Team("Team 1", [ethan, omar])
twoTeam2 = Team("Team 2", [nhan, timmy])
twoTeam3 = Team("Team 3", [stephon, jon])
twoTeam4 = Team("Team 4", [jeff, andrew])
twoTeam5 = Team("Team 5", [jake, kat])
twoTeam6 = Team("Team 6", [rodney, manny])
twoTeam7 = Team("Team 7", [jimmy, yanis])
twoTeam8 = Team("Team 8", [tyler, trevor])
twoTeam9 = Team("Team 9", [cameron, alex])
twoTeam10 = Team("Team 10", [sharon, melanie])
twoTeam11 = Team("Team 11", [kat2, krystal])
twoTeam12 = Team("Team 12", [becca, caroline])
teams2s = [twoTeam1, twoTeam2, twoTeam3, twoTeam4, twoTeam5, twoTeam6, twoTeam7, twoTeam8, twoTeam9, twoTeam10, twoTeam11, twoTeam12]


roster = [sharon, ]


tournament = Tournament([], 21)
season = Season(teams2s)