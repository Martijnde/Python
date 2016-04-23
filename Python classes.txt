#Create a class called Team. Inside the class, create a name property. Assign the value "Tampa Bay Buccaneers" to this property.
#Create an instance of the Team class, and assign it to the variable bucs. Print the name property of the bucs instance.

class Team():
    def __init__(self):
        self.name = "Tampa Bay Buccaneers"
    

bucs = Team()

print(bucs.name)


#Add an instance method called count_total_wins to the Team class. The method should take no arguments (except self), and should return the number 
#of games the team won from 2009-2013. Use the instance method to assign the number of wins by the "Denver Broncos" to broncos_wins.
#Use the instance method to assign the number of wins by the "Kansas City Chiefs" to chiefs_wins.

import csv

f = open("nfl.csv", 'r')
nfl = list(csv.reader(f))

# The nfl data is loaded into the nfl variable.
class Team():
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)
        
    # Your method goes here
    
    
bucs = Team("Tampa Bay Buccaneers")
bucs.print_name()
class Team():
    def __init__(self, name):
        self.name = name
    
    def print_name(self):
        print(self.name)

    def count_total_wins(self):
        count = 0
        for row in nfl:
            if row[2] == self.name:
                count = count + 1
        return count

broncos = Team("Denver Broncos")
broncos_wins = broncos.count_total_wins()

chiefs = Team("Kansas City Chiefs")
chiefs_wins = chiefs.count_total_wins()