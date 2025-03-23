import random

def mad_libs():
    print("Let's play Mad Libs! Fill in the blanks.")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

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

mad_libs()