# sets a value to a variable
types_of_people = 10
# sets a formated string to x, targeting the variable above
x = f"There are {types_of_people} types of people"

# sets a sting to a variable
binary = "binary"
do_not = "don't"
# sets a formated string to x, targeting the variables above
y = f"Those who know {binary} and those who {do_not}."

# prints both variables x and y, with formated strings
print(x)
print(y)

# prints both x and y imbedded in a string
print(f"I said: {x}")
print(f"I also said: '{y}'")

# sets a boolean value to a variable
hilarious = False
# sets a string to a variable, with a empty {}
joke_evaluation = "Isn't that joke so funny?! {}"

# prints the string and formats the empty {} using .format()
print(joke_evaluation.format(hilarious))

# sets a string to a variable
w = "This is the left side of..."
e = "a sting with a right side."

# combines 2 vairables containing strings
print(w + e)
