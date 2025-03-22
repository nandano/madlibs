def mad_libs():
    print("Let's play Mad Libs! Fill in the blanks.")

    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    story = f"Today, I went to the {place} and saw a {adjective} {noun}. \
It suddenly started to {verb}, and everyone was shocked!"
    
    print("\nHere is the story you made:\n")
    print(story)

mad_libs()