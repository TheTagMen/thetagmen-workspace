#!/usr/bin/python3.7
# -*-coding:Utf-8 -*

#Program objective : find if a year input by a user is a leap year

year = input("Ecrivez une année :")    #asking for input

test1 = year % 4						#Prepearing the tests for the 3 conditions
test2 = year % 100
test3 = year % 400

if test1 == 0 and test2 != 0 or test3 == 0: 		#Testing if a year is a leap year
	print("L'année est bissextile")
else:
	print("L'année n'est pas bissextile")