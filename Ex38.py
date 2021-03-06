# http://learnpythonthehardway.org/book/ex38.html

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("There are not 10 things in that list, let's fix that.")

stuff = ten_things.split(" ")
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding ", next_one)
    stuff.append(next_one)
    print("There are %d items right now." % len(stuff))

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(stuff, "\n")
print(' '.join(stuff))
print(type(' '.join(stuff)))
print('#'.join(stuff[3:5]))