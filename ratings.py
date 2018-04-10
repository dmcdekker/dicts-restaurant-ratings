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
            

r = ratings("scores.txt")



def add_rating(rest_ratings):
    rest_name = raw_input("Enter the name of the restaurant: ")
    rating = int(raw_input("Enter the restaurant rating: "))
    while rating > 5 or rating < 1:
        rating = int(raw_input("Rating must be between 1 and 5: reenter the restaurant rating: "))


    rest_ratings[rest_name] = rating

    for restaurant, score in sorted(rest_ratings.iteritems()):
            print "{} is rated at {}".format(restaurant, score)

add_rating(r)
            



