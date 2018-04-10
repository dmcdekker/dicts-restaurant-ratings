"""Restaurant rating lister."""
import random

def ratings(filename):
    rest_ratings = {}
   
    with open(filename) as file_:
        for line in file_:
            restaurant, rating = line.split(":")
            rest_ratings[restaurant] = rating.strip()

    return rest_ratings


def add_rating(rest_ratings):
    print "What would you like to do:"
    choice = int(raw_input("Enter 1 to see all restaurant ratings, 2 to add a " +
        "new restaurant, 3 to update a random restaurant, 4 to update a restaurant of your choosing" +
        " or 5 to quit. "))

    while choice != 5:
        if choice == 1:
            for restaurant, score in sorted(rest_ratings.iteritems()):
                print "{} is rated at {}".format(restaurant, score)

        elif choice == 2:
            rest_name = raw_input("Enter the name of the restaurant: ")
            rating = int(raw_input("Enter the restaurant rating: "))
            while rating > 5 or rating < 1:
                rating = int(raw_input("Rating must be between 1 and 5: reenter " + 
                    "the restaurant rating: "))
            rest_ratings[rest_name] = rating

        elif choice == 3:
            random_rest = random.choice(rest_ratings.keys())
            new_rating = int(raw_input("Enter a new rating for {}: ".format(random_rest)))
            while new_rating > 5 or new_rating < 1:
                new_rating = int(raw_input("Rating must be between 1 and 5: reenter " + 
                    "the restaurant rating: "))
            rest_ratings[random_rest] = new_rating
            print "Thanks for updating the rating!"

        elif choice == 4:
            rest_choice = raw_input("Please choose a restaurant to update: ")
            while rest_choice not in rest_ratings.keys():
                print "That restaurant is not yet in our database!"
                rest_choice = raw_input("Please choose an existing restaurant to update: ")
            new_rating = int(raw_input("Enter a new rating for {}: ".format(rest_choice)))
            while new_rating > 5 or new_rating < 1:
                new_rating = int(raw_input("Rating must be between 1 and 5! Reenter " + 
                    "the restaurant rating: "))
            rest_ratings[new_rating] = new_rating
            rest_ratings[rest_choice] = new_rating
            print "Thanks for updating the rating!"

        print "What would you like to do:"
        choice = int(raw_input("Enter 1 to see all restaurant ratings, 2 to add a " +
            "new restaurant, 3 to update a random restaurant, 4 to update a restaurant of your choosing" +
            " or 5 to quit. "))
    return


r = ratings("scores.txt")
add_rating(r)
