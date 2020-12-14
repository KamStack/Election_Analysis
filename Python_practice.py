print("Hello World")
counties = ["Arapahoe","Denver","Jefferson"]
counties.append("El Paso")
print(counties [3])

#Creating dictionaries
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

#Get all key Value
counties_dict.items()

#to get only keys
counties_dict.keys()

#to get only the values
counties_dict.values()

#Get a specific value
counties_dict.get("Denver")

#another way of getting a specifica value from a key
counties_dict['Arapahoe']
#or
counties_dict["Arapahoe"]

#Create a list called voting data
voting_data = []

#add voting data to the Voting data [] dictionary above
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")



#Conditionals with Dictionaries "If statement"
counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

#Conditionals with Dictionaries "If-else statement"
temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")


#More Conditionals. "If-else and if-elif-else"
#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')


# RE-write using a if-elif-else

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')


# Membership Operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")


#Logical operators USING AND
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

#Logical operators USING OR
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")



#Loops
for county in counties:
    print(county)

#Loops with range
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)
#VS
for num in range(5):
    print(num)

#interating using INDEX
for i in range(len(counties)):
    print(counties[i])

#Using a For Loop to get to iterate over a list or tuple
for county in counties_dict:
    print(county)

#Using a For Loop to get to iterate over a list or tuple for KEYs Only
for county in counties_dict.keys():
    print(county)

#Using a For Loop to get to iterate over a list or tuple for Value Only
for voters in counties_dict.values():
    print(voters)

#Using the Key "County" to reference the Value
for county in counties_dict:
    print(counties_dict[county])

#Using the get Method to get the value of key
for county in counties_dict:
    print(counties_dict.get(county))

#Printing the key_value pairs with a loop
for key, value in counties_dict.items():
    print(key, value)
#OR
for county, voters in counties_dict.items():
    print(county, voters)

# When iterating over a dictionary:

# The first variable declared in the for loop is assigned to the keys.
# The second variable is assigned to the values.

#Iterating over dictionary data using loop
for county_dict in voting_data:
    print(county_dict)

#Get the values from a list of Dictionaries using a nested For loop
# First, use the for loop: for county_dict in voting_data: to retrieve each dictionary. 
# Then, in the second for loop, use the values() method on the variable county_dict to reference the data in the 
# second for loop in order to get each value.
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#If we only want to print the county name from each dictionary, we can use county_dict['county']
#in the print statement for the for loop.
for county_dict in voting_data:
    print(county_dict['county'])


#F String VS "+" Concatenation  
#Concatenation
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

#VS F-String
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Concatenation with dictionaries
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

#F-string with dictionaries
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Multi-line F-String
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

#Formating decimal places with F-String
#f'{value:{width},.{precision}}'

#For Example. Where :2F shows to two decimal places
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")


#Dependencies
# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)

#The Dependency module can also be changed/alias during the import
# Import the datetime class from the datetime module.
import datetime as dt
# Use the now() attribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)

#Putting dependencies to use by using the CSV import
import csv
dir(csv)


#Working witha file in Python
#Direct File Vs Indirect File

#Direct File
# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'


# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()
    

#Formatting the file with the "With statement"
#with open(filename) as file_variable:

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)


#The os module allows us to interact with our operating system. 
# We can see all the different attributes and methods that the os module uses by importing the module and typing print(dir(os)) in the Python interpreter.

import os
dir(os.path)

#Chaining
os.path.join("Resources", "election_results.csv")

#Reference the path of the file
file_to_load = os.path.join("Resources", "election_results.csv")

# Let's put all of this to practical use! In the VS Code PyPoll.py file, complete the following steps:

# Import the csv and os modules.
# Add the filename variable that references the path to election_results.csv.
# Open the election_results.csv using the with statement as the filename object, election_data.
# Print the filename object.
# Your PyPoll.py file should look like this:

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Print the file object.
     print(election_data)


#Write to files in python
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")



