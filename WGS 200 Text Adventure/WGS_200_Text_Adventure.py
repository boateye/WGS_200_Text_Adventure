import textwrap

# Variables, dictionaries, lists, and text strings pertinent to this project

# Dictionaries
credits = {
    'Jordan Johnson' : 'Programmer / Philogynist',
    'Miriam Gonzales' : 'Writer / Misspeller',
	'Sirena Bevilaqua' : 'Writer / Mermaid',
	'Sandra F' : 'Writer / Idea Woman',
	'Sam Burke' : 'Writer / Friendly Neighborhood Bad-ass'}

avatars = {
           '1' : 'Taylor Swift',
           '2': 'Chris Evans',
           '3' : 'Boy George'}

# Lists
list_of_avatars = [
           '1 : Taylor Swift',
           '2 : Chris Evans',
           '3 : Boy George']

# Choices are going to be universal in all situations. However, responses to said choices will differnt depending on the selected toon. This should cut down on development time, and provice a deeper message.
sit1Choices= [
              "1. I think that I'd be able to provide excellent moral support to our troops.",
              "2. Controlling those unmanned drones is like playing a video game, right?",
              "3. I've seen Tropic Thunder, and I know I'm better prepared than THOSE guys!"]

# Text String Variables
Toon = 0
choice = ""

pregame = """Welcome to our WGS 2000 Creative Project! You are about to embark on a "choose your own adventure" style game. There are no right or wrong descisions. Only choices, and consequences. If you're lost, just type 'help'. Enjoy! """
pregame_paragraph = textwrap.wrap(pregame, width = 70)

introduction = """You're lying in your bed. It's a beautiful morning in San Francisco; the birds are chirping, the sun is shining, and you survived last night's all-nighter with nary a hangover. Your cell rings, and it's a call from some government number. You answer. A recorded voice says, "Hello %s, this is the US Military. You have been selected in the most recent draft as a candidate to serve your country. Please report to your nearest deafting outpost for your pre-enlistment interview, ASAP." Reluctantly, you rise out of bed. You find the nearest outpost online, and head there after your morning routine. You are greeted at the outpost by a decorated US soldier. "Hello %s, I am Commander Sheperd. Please have a seat." """ % (Toon, Toon)
introduction_paragraph = textwrap.wrap(introduction, width = 70)

# a function that defines how the game process input stored as the variable: 'command'
def process(command):
    str(command)
    command.lower()
    if command == "help":
            print "To make a descision, just enter the corresponding number next to your choice"
            print "Type 'about' if you want to know who helped to make this project!"
            input()
    elif command == "about":
        for person in credits:
            print "%s : %s" % (person, credits[person])
    elif len(command) >= 1:
        return command
    else:
        print "%s is not a valid command" % command
        hinput()

#a function that asks the user for input

def input():
    command = raw_input("What do you want to do?")
    process(command)
    return command

#defines a function that will greet the user
def start():
    for pregameLine in pregame_paragraph:
        print pregameLine  
    print ""
    print "Before we start, please choose your character:"
    print ""
    for avatar in list_of_avatars:
        print avatar
        print ""
#player chooses avatar
    choice = raw_input("Who do you choose?")
    process(choice)
    if choice == "1":
        print ""
        print "Greetings Ms. Swift!"
        print ""
        Toon = "Taylor Swift"
        sit1()
    elif choice == "2":
        print ""
        print "Salutations, Mr. Evans!"
        print ""
        Toon = "Chris Evans"
        sit1()
    elif choice == "3":
        print ""
        print "How do you do, Boy George!"
        print ""
        Toon = "Boy George"
        sit1()
    else:
        print "That is not a valid choice."
        choice = raw_input("Who do you choose?")


#Introduction to first situation
def sit1():

    for introLine in introduction_paragraph:
        print introLine
    print ""
    print """ "So, how do you see yourself serving your country?" Commander Sheperd asks"""
#First Descision
    for sit1choice in sit1Choices:
        print ""
        print sit1choice
        print ""
    choice = raw_input("What do you say?")
    process(choice)
    print choice
    print Toon
#TSwift Responses
    if choice == "1" and Toon == "Taylor Swift":
        print "I agree. Many of troops like yourself excel in the supportive roles. Not everyone is fit for combat."
        print "But I think that I'd be great in combat, too! I didn't know that was an option..."
        print "I don't think that's such a good idea."
        print "Why?"
        print "Because, you'd be a distraction for your fellow troops."
    elif choice == "2" and Toon == "Taylor Swift":
        print "Pretty much. Did your brother, teach you how to play those games?"
        print "I'm an only child."
        print "Father, then?"
        print "I taught myself"
        print "Good for you!"
    elif choice == "3" and Toon == "Taylor Swift":
        print "Everyone is more prepared than those men."
        print "Also, Robert Downey Jr. looked great in that film. then again, does ne ever look bad?"
        print "You're right, he's one handsome man. Anyway, this is not Vietname, nor is it a movie about war. This is a real war, and I don't think that there you'd be a good fit."
        print "But I can be the dude playing the dude, disguised as another dude!"
        print "Please leave, Ms. Swift. You're just unfit for this war."
#CEvans Responses
    elif choice == 1 and Toon == "Chris Evans":
        print "And you probably would. However, don't you think that you'd be a better fit on the front lines?"
        print "I get Queasy around blood."
        print "You serious?"
        print "Yea. I cut my knee last week, and fainted. Luckily, my roomate found me bleeding on the floor and passed out. I woke up, cleaned and with a band aid on my knee. It has Captain america on it!"
        print "That's a good film"


    

#Game starts here
start()
