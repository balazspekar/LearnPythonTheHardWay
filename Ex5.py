# http://learnpythonthehardway.org/book/ex5.html

my_name = 'Balazs Pekar'
my_age = 28
my_height = 180
my_weight = 90
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %r." % (my_name))
print("He's %d centimeters tall." % (my_height))
print("He's %d kgs heavy." % (my_weight))
print("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." % my_teeth)

print("If I add %d, %d and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight))

print("Rounding: ", round(1.477))