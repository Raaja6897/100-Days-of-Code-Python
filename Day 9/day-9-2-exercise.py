travel_log=[
    {
        "country": "France",
        "visits": 12,
        "cities":["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Donot change the code above
#TODO: Write a function that will allow new countries
#to be added to travel_log

def add_new_country(country, visits, cities):
    add = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(add)

# Method 2 from udemy course
"""
def add_new_country(country_visited, times_visited, cities_visited):
    mew_country={}
    new_country["country"] = country_visited
    new_country["visited"] = times_visited
    new_country["ciites"] = cities_visited
    travel_log.append(new_country)
"""

add_new_country("Russia",2,["Moscow", "Saint Peterburg"])
print(travel_log)