# http://learnpythonthehardway.org/book/ex39.html

states = {'Oregon' : 'OR',
          'Florida' : 'FL',
          'California' : 'CA',
          'New York' : 'NY',
          'Michigan' : 'MI'}


cities = {'CA': 'San Francisco',
          'MI': 'Detroit',
          'FL': 'Jacksonville'}

cities["NY"] = "New York"
cities["OR"] = "Oregon"

print("*" * 40)
print("NY state has:", cities["NY"])

print("*" * 40)
print("Michigan abbrevation is:", states["Michigan"])

print("*" * 40)
print("Michigan has:", cities[states['Michigan']])

print("*" * 40)
print("*" * 40)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

print()
print(states.items())

jancsi = states.items()
print(type(jancsi))
