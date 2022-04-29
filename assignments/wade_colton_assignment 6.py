# Colton Wade Assignment 6

import random  # Imports Random

# states dictionary
states = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": " Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virgina": "Richmond",
    "Washington": "Olympia",
    "West Virgina": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne"
}

# Creates Right/Wrong Counters
right = 0
wrong = 0

# While Loop
while True:

    state = random.choice(list(states))  # Gets a random state, from the states dictionary
    capital = states[state]  # sets capital equal to the value of state

    # Asks for user to input the capital of the state or press 0 to quit
    answer = str(input("What is the capital of {0}? (Or enter 0 to quit): ".format(state)))

    # This if statement goes first so it will it wont count as a wrong answer.
    # If user enters 0 it will quit print the results and end the loop
    if answer == "0":
        print("You had {0} Correct, and {1} Incorrect.".format(right, wrong))
        break
    if answer == capital:
        print("Correct!")
        right += 1  # If user answers right it will add one to right
    else:
        print("Incorrect!")
        wrong += 1  # If user answers wrong it will add one to wrong