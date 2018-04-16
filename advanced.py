"""Restaurant rating lister."""

import random
import os, sys

def get_files():
    """ Get txt files from current directory"""
    documents = []
    for filename in os.listdir('.'):
        if os.path.isfile(filename) and filename[-3:] == 'txt':
            documents.append(filename)
    return documents

def select_file(data):
    """ Allows user to Select a file"""
    for index, filename in enumerate(data):
        print index+1, filename
    data_number = int(raw_input("Select a file # or press enter to exit"))
    return data[data_number-1]

def process_scores(filename):
    """Read scores file and return dictionary of {restaurant-name: score}."""

    scores_txt = open(filename)

    scores = {}

    for line in scores_txt:
        line = line.rstrip()
        restaurant, score = line.split(":")
        scores[restaurant] = int(score)

    return scores


def get_action_choice():
    """Gives the user a choice of actions and returns the user's choice.

   Choice 1: See ratings
   Choice 2: Add a new restaurant
   Choice 3: Re-rate a random restaurant
   Choice 4: Re-rate a chosen restaurant
   Choice 5: Quit
    """

    print
    print "What would you like to do?"
    print "    1: See ratings for all restaurants"
    print "    2: Add a new restaurant"
    print "    3: Re-rate a random restaurant"
    print "    4: Re-rate a specific restaurant"
    print "    5: Quit"

    return int(raw_input("> "))


def add_restaurant(scores):
    """Add a restaurant and rating."""

    restaurant = raw_input("Restaurant name> ")
    score = get_score("Rating> ")
    scores[restaurant] = score


def get_score(prompt):
    """Prompt for a valid score."""

    while True:
        entry = raw_input(prompt)

        if not entry.isdigit():
            continue

        rating = int(entry)

        if rating >=1 and rating <= 5:
            return rating


def rate_random_restaurant(scores):
    """Rate restaurants in a loop until user quits."""

    # pick a random restaurant key
    restaurant, rating = random.choice(scores.items())

    print "The current rating for {} is {}.".format(restaurant, rating)
    new_rating = get_score("What is your rating for %s? " % restaurant)

    scores[restaurant] = new_rating


def rate_specific_restaurant(scores):
    """Give the user a choice of which restaurant to re-rate."""

    # show user the current scores
    print_sorted_scores(scores)

    while True:
        print "\nWhich restaurant would you like to update?"
        print "Please enter the name exactly as it appears above."
        restaurant = raw_input("> ")

        # if their input was valid, prompt for a new rating

        if restaurant in scores:
            rating = scores[restaurant]
            print "The current rating for %s is %d." % (restaurant, rating)
            new_rating = get_score("What is your rating for %s? " % restaurant)

            # the input was valid so we don't need to ask again
            break

        # otherwise, prompt them again
        print "That's not one of the restaurants above. Please try again."

    # update the scores dictionary
    scores[restaurant] = new_rating


def print_sorted_scores(scores):
    """Print sorted dictionary."""

    print
    for restaurant, rating in sorted(scores.iteritems()):
        print "{} is rated at {}.".format(restaurant, rating)


# read existing scores in from file

files = get_files()
if files != '':
    sys.exit()
filename = select_file(files)
scores = process_scores(filename)
while True:
    while True:
        # present the user with a menu of options and get their choice
        action = get_action_choice()

        # act accordingly
        if action == 1:
            print_sorted_scores(scores)

        elif action == 2:
            add_restaurant(scores)

        elif action == 3:
            rate_random_restaurant(scores)

        elif action == 4:
            rate_specific_restaurant(scores)

        elif action == 5:
            print "Goodbye!"
            break
        else:
            print "Invalid input. Please try again."
    files = get_files()
    if files != '':
        filename = select_file(files)
        scores = process_scores(filename)
    else:
        break
