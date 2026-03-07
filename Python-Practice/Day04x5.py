#Store details of n movies in a dictionary by taking input from the user. Each movie must store details like name,  year, director name, production cost, collection made (earning) & perform the following :- a)print all movie details. b)display name of movies released before 2015. c)print movies that made a profit. d)print movies directed by a particular director.

n = int(input("Enter number of movies: "))
movies = {}

for i in range(n):
    print("\nEnter details for movie", i+1)
    name = input("Movie Name: ")
    year = int(input("Year: "))
    director = input("Director: ")
    cost = float(input("Production Cost: "))
    collection = float(input("Collection: "))
    
    movies[name] = {
        "year": year,
        "director": director,
        "cost": cost,
        "collection": collection
    }

print("\nAll Movie Details:")
for name, details in movies.items():
    print(name, ":", details)

print("\nMovies released before 2015:")
for name, details in movies.items():
    if details["year"] < 2015:
        print(name)

print("\nMovies that made profit:")
for name, details in movies.items():
    if details["collection"] > details["cost"]:
        print(name)

director_name = input("\nEnter director name to search: ")
print("Movies directed by", director_name + ":")

for name, details in movies.items():
    if details["director"].lower() == director_name.lower():
        print(name)