import textwrap
import time
import os
# Variables, dictionaries, lists, and text strings pertinent to this project

# Dictionaries
credits = {
    'Jordan Johnson' : 'Programmer / Philogynist',
    'Miriam Gonzales' : 'Writer / Misspeller / Rabbit Soup Connoisseur',
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
           '2 : Chris Evans']
#           '3 : Boy George']

# Choices are going to be universal in all situations. However, responses to said choices will differnt depending on the selected toon. This should cut down on development time, and provice a deeper message.
sit1Choices = [
              "1. I think that I'd be able to provide excellent moral support to our troops.",
              "2. Controlling those unmanned drones is like playing a video game, right?",
              "3. I've seen Tropic Thunder, and I know I'm better prepared than THOSE guys!"]
sit1Choices2 = [
                "1. I would tell him that if they don't want to be in the meeting, then they can leave, becasue they are distracting, not only me, but their coworkers",
                "2. People only do that for attention, so if I don't give him any during the meeting, then he should settle down. Ergo, I'd try to continue with the meeting, and, afterwards, I'de to talk afterwards." ]

# Text String Variables
Toon = ""
choice = ""

pregame = """Welcome to our WGS 200 Creative Project! You are about to embark on a "choose your own adventure" style game. There are no right or wrong descisions. Only choices, and consequences. If you're lost, just type 'help'. Enjoy! """
pregame_paragraph = textwrap.wrap(pregame, width = 70)

# a function that will make wrapping an individual line easier

def wrap(string):
    str(string)
    x = string
    
    y = textwrap.wrap(x)
    
    for z in y:
        print z

# a function that defines how the game process input stored as the variable: 'command'
def process(command):
    str(command)
    command.lower()
    if command == "help":
        print ""
        wrap("To make a decision, just type the corresponding number next to your choice, and then press enter.")
        print""
        wrap("Type 'about' if you want to know who helped to make this project!")
        print""
        wrap("Type 'reset' to start over")
        print""
    elif command == "about":
        for person in credits:
            print "%s : %s" % (person, credits[person])
    elif command == "reset":
        os.system("cls")
        start()
    elif len(command) >= 0:
        return command
    else:
        print "%s is not a valid command" % command
        process(command)
        #input()

#a function that asks the user for inputv (i don't think this is necesary, since i created a  process(command) function

#def input():
#    #command = raw_input(">")
#    process(command)
#    return command

#defines a function that will initialize the game

def start():
    for pregameLine in pregame_paragraph:
        wrap(pregameLine)  
    print ""
    #time.sleep(7)
    pause = raw_input("Press ENTER to continue")
    print "Before we start, please choose your character:"
    print ""
    for avatar in list_of_avatars:
        print avatar
        print ""
    chooseavatar()

#defines a fucntion for choosing an avatar
def chooseavatar():
    choice = raw_input(">")
    process(choice)
    global Toon
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
#    elif choice == "3":
#        print ""
#        print "How do you do, Boy George!"
#        print ""
#        Toon = "Boy George"
#        sit1()
    else:
        print "That is not a valid choice."
        chooseavatar()


#Introduction to first situation
def sit1():
    introduction = """You're lying in your bed. It's a beautiful morning in San Francisco; the birds are chirping, the sun is shining, and you survived last night's all-nighter with nary a hangover. Your cell rings, and it's a call from some government number. You answer. A recorded voice says, "Hello %s, this is the US Military. You have been selected in the most recent draft as a candidate to serve your country. Please report to your nearest deafting outpost for your pre-enlistment interview, ASAP." Reluctantly, you rise out of bed. You find the nearest outpost online, and head there after your morning routine. You are greeted at the outpost by a decorated US soldier. "Greetings %s, I am Commander Sheperd. Please have a seat." """ % (Toon, Toon)
    introduction_paragraph = textwrap.wrap(introduction, width = 70)
    for introLine in introduction_paragraph:
        print introLine
    print ""
    print """ "So, how do you see yourself serving your country?" Commander Sheperd asks"""
    pause = raw_input("Press ENTER to Continue")
#First Descision
    for sit1choice in sit1Choices:
        print ""
        print sit1choice
        print ""
    choice = raw_input(">")
    process(choice)
#TSwift Responses
    if choice == "1" and Toon == "Taylor Swift":
       print 
       wrap(""""I agree. Many troops, like yourself, excel in the supportive roles. Not everyone is fit for combat, you know," Sheperd states.""")
       print 
       wrap(""""But I think that I'd be great in combat, too! I didn't know that was an option..." you retort.""")
       print 
       wrap(""""I don't think that's such a good idea." """)
       print 
       wrap(""""Why?" """) 
       print 
       wrap(""""Because, you'd be a distraction for your fellow troops." """) 
       print 
       sit1_2()
    elif choice == "2" and Toon == "Taylor Swift":
        print""
        print """"Pretty much. Did your brother teach you how to play those games?" """
        print ""
        print """"I don't have a brother. I'm an only child." """
        print ""
        print """"Friend, then?" """
        print ""
        print """ None of my friends played before I introduced them." """
        print ""
        print """I find that hard to believe, but anyway..." """
        print""
        sit1_2()
    elif choice == "3" and Toon == "Taylor Swift":
        wrap(""""Everyone is more prepared than those men." """)
        print""
        wrap(""""Also, Robert Downey Jr. looked great in that film. then again, does he ever look bad?" """)
        print ""
        wrap(""""You're right, he's one handsome man. Anyway, this is not Vietname, nor is it a movie about war. This is a real war, and I don't think that there you'd be a good fit." """)
        print ""
        wrap(""""But I can be the dude playing the dude, disguised as another dude!" """)
        print ""
        wrap(""""Please leave, Ms. Swift. You're just unfit for this war." """)
        print ""
        sit1_2()
#CEvans Responses
    elif choice == "1" and Toon == "Chris Evans":
        print
        wrap(""""And you probably would. However, don't you think that you'd be a better fit on the front lines?" """)
        print
        wrap(""""I get Queasy around blood." """)
        print 
        wrap("""You serious?" " """)
        print 
        wrap(""""Yea. I cut my knee last week, and fainted. Luckily, my roomate found me bleeding on the floor and passed out. I woke up, cleaned and with a band aid on my knee. It has Captain america on it!" """)
        print 
        wrap(""""That's a good film" """)
        sit1_2()
    elif choice == "2" and Toon == "Chris Evans":
        print
        wrap(""""Basically. It's like playing a deadlier version of Microsoft Flight Simulator" """)
        print
        wrap(""""Oh yea I played that. I'm more of a Call of duty guy, though." """)
        print 
        wrap(""""Well there's no respawning in this, just keep that in mind, haha" """)
        sit1_2()
    elif choice == "3" and Toon == "Chris Evans":
        print
        wrap(""""You could be the dude playing the dude, disguised as another dude!" """)
        print
        wrap(""""Unfortunately, I'm no Robert Downey Jr. He is one handsome man, though" """)
        print
        wrap(""""Excuse me?" """)
        print
        wrap(""""Robert Downey. He's an attractive man." """)
        print
        wrap(""""Yes, but that kind of talk is not appropriate for someone who will be representing our country" """)
        print
        wrap(""""Sorry." """)
        sit1_2()
# Part 2 of the drafting situation
def sit1_2():
    print
    wrap(""""Next situation," Digresses Commander Sheperd "You're giving a presentation for a meeting at your job. Throughout the meeting, the one of your male coworkers is being a bit...distracting. It's very disruptive to your presentation. How do you handle this situation?" """)
    print
    #time.sleep(7)
    pause = raw_input("Press ENTER to continue")
    for choice in sit1Choices2:
        wrap(choice)
        print
    choice = raw_input(">")
    process(choice)
    if choice == "1" and Toon == "Taylor Swift":
        print
        wrap(""""Interesting. However, don't you think that's a bit...direct?" """)
        print
        wrap(""""Yes, because he was being disruptive.  It needs to be nipped in the bud." """)
        print
        wrap(""""True, but it might be better to be a bit gentler. I mean, you want people to take you seriously." """)
    elif choice == "2" and Toon == "Taylor Swift":
        print
        wrap(""""That's probably a good idea. You don't want to put yourself in danger." """)
        print
        wrap(""""What do you mean?" """)
        print
        wrap(""""I mean, you made a safe choice. He's proably bigger than you, anyway." """)
    elif choice == "1" and Toon == "Chris Evans":
        print
        wrap(""""That's a good way to deal with the situation. It shows great leadership!" """)
    elif choice == "2" and Toon == "Chris Evans":
        print
        wrap(""""That's an...intersting response. Don't get me wrong, your coworker is probably doing it for attention, but you shouldn't let him detract from your presentation." """)
        print
        wrap(""""In my experience, either other people will admonish the disruptive person, or their activity will deflate once you deprive them of attention." """)
        print
        wrap(""""How about a more direct approach? I mean, you want to be good leader, don't you? Besides, people will lsiten to you." """) 


    
#Game starts here
start()



