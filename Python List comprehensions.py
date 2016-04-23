#In the last mission, we worked with with legislators.csv, which contains information on every historical US Congressperson. 
#In the last mission, we cleaned up some missing data and added an additional birth year column.
#We'll continue to work with the same dataset in this mission. Here's the beginning of the dataset, in csv format:
last_name -- the last name of the Congressperson.
•first_name -- the first name of the Congressperson.
•birthday -- the birthday of the Congressperson.
•gender -- the gender of the Congressperson.
•type -- whether the Congressperson was in the Senate (sen), or in the House of Representatives (rep).
•state -- the state the Congressperson represents.
•party -- the party affiliation of the Congressperson.
•birth_year -- the year the Congressperson was born. This column is an integer value.

ships = ["Andrea Doria", "Titanic", "Lusitania"]
cars = ["Ford Edsel", "Ford Pinto", "Yugo"]
#Enumerate the ships list using a for loop and the enumerate() function.
#In each iteration of the loop:◦Print the item from ships at the current index
#Print the item from cars at the current index.
for i, ship in enumerate(ships):
    print(ship)
    print(cars[i])

	
things = [["apple", "monkey"], ["orange", "dog"], ["banana", "cat"]]
trees = ["cedar", "maple", "fig"]
#Loop through each row in things using the enumerate() function.
#Append the item in trees with the same index to the end of each row in things.
#At the end, things should have an extra column
for i, thing in enumerate(things):
    thing.append(trees[i])


apple_prices = [100, 101, 102, 105]
#Create a new list called apple_prices_doubled where each item in apple_prices is multiplied by 2
apple_prices_doubled = [(price * 2) for price in apple_prices]
#Create a new list called apple_prices_lowered where 100 is subtracted from each item in apple_prices
apple_prices_lowered = [(price - 100) for price in apple_prices]


