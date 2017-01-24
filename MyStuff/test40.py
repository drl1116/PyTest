# --coding:utf-8--
things = ['a', 'b', 'c', 'd']
print things[1]

things[1] = 'z'
print things[1]

print things


stuff = {'name': 'Zed', 'age': 36, 'height': 6 * 12 + 2}
print stuff['name']
print stuff['age']
print stuff['height']

stuff['city'] = "San Francisco"
print stuff['city']

stuff[1] = "Wow"
stuff[2] = "Neato"
print stuff[1]
print stuff[2]
print stuff

del stuff['city']
del stuff[1]
del stuff[2]
print stuff

# 正式练习
cities = {'CA': 'San Franciso', 'MI': 'Detroit', 'FL': 'Jacksonville'}

cities['NY'] = "New York"
cities['OR'] = 'Portland'


def find_city(themap, state):
    if state in themap:
        return themap[state]
    else:
        return "Not Found."


# ok pay attention!
cities['_find'] = find_city

while True:
    print "State? (Enter to quit)",
    state = raw_input("> ")
    if not state:
        break

    # this line is the most important ever! study!
    city_found = cities['_find'](cities, state)
    print city_found
