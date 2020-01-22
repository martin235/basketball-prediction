
Here are the instructions to run the program, if you have any questions about the program just send me a message via github. or send me an email at martin.bacques.mb@gmail.com.
I'm not explaining here the way I've made the machine learning but I can help you if you want or maybe just advise you some documentations.
I apology if there is no comments on the code but I will maybe change that. I'm french so the name of the variable and the fuction are in french.

As a fan of NBA this code has been made to predict NBA games using machine learning.
There is 6 python files to use:

1- ScraperCalender2019-2020.py:
	This file is made to take the games that have been played and the games that are going to been played in this month, don't forgot to add month in the list "month" if you change month.
	The number of games that have been played in this month is in the variable "nbMatchs" which stands for "number of games"
	This file save the information in the file "scrapperCalender2019-2020.pickle"
	The program ask you "Initialisation?" just responds "oui" ("yes" in french)

2-ScrappingDataNBA2019-2020.py:
	This file is made to take the main information from all the 30 nba teams. The data that takes this progam are the name of the team, wins, loses, percentage of wins,
	offense average (points), defense average (points).
	This program need to be updated evrey day if you want the freshest data.
	This program save the information in "Stat2019-2020.pickle".

3-CoteProno.py:
	This file is taking the games betting odds from a french bet site so if you want to change to an other site just ask me and I'll do that for you but you can also keep this one.
	When the program ask you "Enregistrer?" it means "Save?" so you just need to enter "oui"
	It saves the information in CoteProno 

4-PronoTK.py:
	This file must be open after CoteProno.py because it runs a program that can let you choose the bet you want to make.
	"Mise" is for the virtual money you want to bet, you just need to enter an integer or a float number. "Domicile" is for the teams who are playing at home, the "Visiteurs" is for the teams who are playing away.
	After entering the money and the bet you want to make, click on "PARIER" which means "bet" and close the window.
	The teams, the money will be saved in PariMoi.pickle
	
5-NeuralNetwork2.py:
	Here is the main program that calculate which teams you need to bet on (There are 4 differents lists that I'll explain you after).
	Make sure you have already updated ScraperCalender2019-2020.py and ScrappingDataNBA2019-2020.py because it will use informations from it.
	When you run the program it will ask you first "Nombre de matchs" which means "Number of games" so you enter the number of games of the day you are. 
	Then the program will ask you "Nombre de matchs déjà joués" which means "Number of games that have been already played" I always enter 0 but you can
	enter the number of games (100 if you don't want to take the games from the beginning of the season). 
	After that the program is going take a bit of time to calculate some things, it will ask you then "Number of epochs" there is no transaltion here you just need to enter the number of times
	the programs is going to calculate, most of the time I use 10 epochs and then it will the number of trys I also enter 10.
	It's going to takes a lot of times to calculate because it will twice 10 epochs with in it 10 trys.
	When it's finish it will print you the lists with the teams that it thinks will win today. The first list is not using machine learning but using simple rules that compares the diferents datas,
	this list is not very accurate. The second list is using maching learning but it will not output more than 2 teams because by experience it is not very accurate when you bet more than 2 teams. 
	The third list is also using machine learning but I've tried tu use more neurons and to use hidden layers. Most of the time it will predict the same teams as the second list.
	The fourth and las list is made by comparing the first and the second list and output the teams that are both in the first and the second list.
	These fours lists are saved in PronoMatch.

6-Prono.py:
	This file is made to save the bet the program and the bet you've made.
	For every questions of the program will ask you just enter "oui".
	The program will save the information in Update.pickle and in prono.txt with a version written of the bet. It will also save the "bonus" you've made by saving it in bonus.pickle.
	The bet multiply the betting odd of all the teams that you are betting on so when a team you bet doesn't win the bet is not passing. The program bet 5 (euros or dollars as you want) and take the rest of money
	you've made the last bet if it passed and if it is more than 10 (euros or dollars) it will save 5 in the bonus. If the bet didn't pass the bonus will be substracted by 5 and the next will be 5 (euros or dollars).
	There is 5 bets which for the four bets of the NeuralNetwork program and the one you've made whith PronoTk.
	This program is made to follow the money you've made. 
	
	
Thanks for reading now you can use the program if you still have questions send me messages, I know my explanations are not very good.
	
