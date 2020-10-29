import random
import time

# Each list contains values. The first list contains the sorting hat phrases and the second list contains Hogwarts Houses
phrases = ["hmmmmmm", "Difficult. Very difficult!", "Where shall I put you?", "Are you sure you're not a muggle? Well then!", "You need to wash your hair!", "You might go Ravenclaw!", "Maybe Slytherin?", "Maybe. Just Maybe."]
house = ["SLYTHERIN!", "HUFFLEPUFF!", "GRYFFINDOR!", "RAVENCLAW!"]

# This loop selects two random numbers
for x in range(1):
  random_phrase = (random.randint(0,7))
  random_house = (random.randint(0,3))


# This input field asks the user what their name is
print("I am the Sorting Hat and I will sort you into your Hogwarts house. \n")
name = input("Come close child. What is your name? \n")

# Generates random phrases and tells the user what house they belong to
print("\n")
print("Hello", name.upper(),"!")
time.sleep(2)
print(phrases[int(random_phrase)])
time.sleep(2)
print("You belong in", house[int(random_house)])
