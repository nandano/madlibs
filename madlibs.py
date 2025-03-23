import random

def get_user_input():
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")
    return adjective, noun, verb, place

def mad_libs():
    print("\nLet's play Mad Libs! Fill in the blanks.\n")

    adjective, noun, verb, place = get_user_input()

    stories = [
        f"I was walking through the {place} when I saw a {adjective} {noun}. \
It suddenly started to {verb}, and I couldn't believe my eyes!",
        f"Today, I went to the {place} and saw a {adjective} {noun}. \
It suddenly started to {verb}, and everyone was shocked!",
        f"At the {place}, I found a {adjective} {noun} that could {verb}! \
Everyone gathered around to watch in amazement.",
]
    story = random.choice(stories)
    
    print("\nHere is the story you made:\n")
    print(story)

while True:
    mad_libs()
    should_quit = input("Do you want to exit the game? (y/n): ")
    if should_quit == 'y':
        print("Thank you for playing Mad Libs!\nHave a nice day.")
        break