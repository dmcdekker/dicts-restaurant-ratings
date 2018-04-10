"""Restaurant rating lister."""


def ratings(filename):
    rest_ratings = {}
    with open(filename) as file_:
        for line in file_:
            restaurant, rating = line.split(":")
            rest_ratings[restaurant] = rating.strip()

        # for restaurant, score in sorted(rest_ratings.iteritems()):
        #     print "{} is rated at {}".format(restaurant, score)

    return rest_ratings

import random    

def add_rating(rest_ratings):
    print "What would you like to do:"
    choice = int(raw_input("Enter 1 to see all restaurant ratings, 2 to add a new restaurant or 3 to update a random restaurant or 4 to quit. "))
    while choice != 4:
        if choice == 1:
            for restaurant, score in sorted(rest_ratings.iteritems()):
                print "{} is rated at {}".format(restaurant, score)
        elif choice == 2:
            rest_name = raw_input("Enter the name of the restaurant: ")
            rating = int(raw_input("Enter the restaurant rating: "))
            while rating > 5 or rating < 1:
                rating = int(raw_input("Rating must be between 1 and 5: reenter the restaurant rating: "))
            rest_ratings[rest_name] = rating
        elif choice == 3:
               random_rest = random.choice(rest_ratings.keys())
               new_rating = int(raw_input("Enter a new rating for {}: ".format(random_rest)))
               rest_ratings[random_rest] = new_rating
               print "Thanks for updating the rating!"


                
        print "What would you like to do:"
        choice = int(raw_input("Enter 1 to see all restaurant ratings, 2 to add a new restaurant or 3 to quit. "))
    return



r = ratings("scores.txt")
add_rating(r)
            



