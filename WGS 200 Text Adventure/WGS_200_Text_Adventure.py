import textwrap
import time
import os
import sys
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
              "2. Controlling those unmanned drones is like playing a video game, right?"]
              #"3. I've seen Tropic Thunder, and I know I'm better prepared than THOSE guys!"
sit1Choices2 = [
                "1. I would tell him that if they don't want to be in the meeting, then they can leave, becasue they are distracting, not only me, but their coworkers",
                "2. People only do that for attention, so if I don't give him any during the meeting, then he should settle down. Ergo, I'd try to continue with the meeting. Afterwards, I'll take him aside and talk to him." ]
sit2Choices = [
               "1. 10oz. T Bone Steak Dinner",
               "2. Soup & Salad special"] 

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
        os.system('cls' if os.name == 'nt' else 'clear')
        start()
    elif len(command) >= 1 and (command == "1" or command == "2"):
       return command
# if the user inputs either nothing or an invalid command
    else:
        print "%s is not a valid command" % command
        command = raw_input(">")
        str(command)
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
        os.system('cls' if os.name == 'nt' else 'clear')
        print ""
        print "Greetings Ms. Swift!"
        print ""
        Toon = "Taylor Swift"
        sit1()
    elif choice == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
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
    introduction = """You're lying in your bed. It's a beautiful morning in San Francisco; the birds are chirping, the sun is shining, and you survived last night's all-nighter with nary a hangover. Your cell rings, and it's a call from some government number. You answer. A recorded voice says, "Hello %s, this is the US Military. You have been selected in the most recent draft as a candidate to serve your country. Please report to your nearest drafting outpost for your pre-enlistment interview, ASAP." Reluctantly, you rise out of bed. You find the nearest outpost online, and head there after your morning routine. You are greeted at the outpost by a decorated US soldier. "Greetings %s, I am Commander Sheperd. Please have a seat." """ % (Toon, Toon)
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
       os.system('cls' if os.name == 'nt' else 'clear')
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
       pause = raw_input("Press ENTER to continue")
       os.system('cls' if os.name == 'nt' else 'clear') 
       sit1_2()
    elif choice == "2" and Toon == "Taylor Swift":
        os.system('cls' if os.name == 'nt' else 'clear')
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
        pause = raw_input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        sit1_2()
#    elif choice == "3" and Toon == "Taylor Swift":
#       wrap(""""Everyone is more prepared than those men." """)
#      print""
#      wrap(""""Also, Robert Downey Jr. looked great in that film. then again, does he ever look bad?" """)
#        print ""
#        wrap(""""You're right, he's one handsome man. Anyway, this is not Vietname, nor is it a movie about war. This is a real war, and I don't think that there you'd be a good fit." """)
#        print ""
#        wrap(""""But I can be the dude playing the dude, disguised as another dude!" """)
#        print ""
#        wrap(""""Please leave, Ms. Swift. You're just unfit for this war." """)
#        print ""
#        pause = raw_input("Press ENTER to continue")
#        os.system('cls' if os.name == 'nt' else 'clear')
#        sit1_2()
#CEvans Responses
    elif choice == "1" and Toon == "Chris Evans":
        os.system('cls' if os.name == 'nt' else 'clear')
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
        pause = raw_input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        sit1_2()
    elif choice == "2" and Toon == "Chris Evans":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        wrap(""""Basically. It's like playing a deadlier version of Microsoft Flight Simulator" """)
        print

        wrap(""""Oh yea I played that. I'm more of a Call of duty guy, though." """)
        print 
        wrap(""""Well there's no respawning in this, just keep that in mind, haha" """)
        pause = raw_input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        sit1_2()
#    elif choice == "3" and Toon == "Chris Evans":
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
        pause = raw_input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        sit1_2()
    else:
        sys.stdout.write ("That is not a valid input")
        process(choice)
# Part 2 of the drafting situation
def sit1_2():
    print
    wrap(""""Next situation," Digresses Commander Sheperd "You're giving a presentation for a meeting at your job. Throughout the meeting, one of your male coworkers is being a bit...distracting. It's very disruptive to your presentation. How do you handle this situation?" """)
    print
    #time.sleep(7)
    pause = raw_input("Press ENTER to continue")
    print
    for choice in sit1Choices2:
        wrap(choice)
        print
    choice = raw_input(">")
    process(choice)
    if choice == "1" and Toon == "Taylor Swift":
        os.system('cls' if os.name == 'nt' else 'clear')
        wrap(""""There are going to be a lot of distractions, Miss Swift. A good skill to have would be to not fall into any temptations of the outside world and continue with your duties, disregarding any diverging noise." """)
        print
        wrap(""""I just think it is important that we tackle issues at hand and try to create a healthy work atmosphere and I believe that being direct and assertive would be the proper way to handle any disruptions." """)
        print
        wrap(""""I do not think that would be considered proper etiquette." """)
        pause = raw_input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        sit2()
    elif choice == "2" and Toon == "Taylor Swift":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        wrap(""""That's probably a good idea. You don't want to put yourself in danger." """)
        print
        wrap(""""What do you mean?" """)
        print
        wrap(""""I mean, you made a safe choice. He's proably bigger than you, anyway." """)
        pause = raw_input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        sit2()
    elif choice == "1" and Toon == "Chris Evans":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        wrap(""""That's a good way to deal with the situation. It shows great leadership!" """)
        pause = raw_input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        sit2()
    elif choice == "2" and Toon == "Chris Evans":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        wrap(""""That's an...intersting response. Don't get me wrong, your coworker is probably doing it for attention, but you shouldn't let him detract from your presentation." """)
        print
        wrap(""""In my experience, either other people will admonish the disruptive person, or their activity will deflate once you deprive them of attention." """)
        print
        wrap(""""How about a more direct approach? I mean, you want to be good leader, don't you? Besides, people will lsiten to you." """) 
        pause = raw_input("Press ENTER to continue")
        os.system('cls' if os.name == 'nt' else 'clear')
        sit2()
# Situation 3 
def sit2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print
    wrap(""""That being said," concludes Commander Sheperd,"I'm going to have to consult with my superiors about your ability to serve your country. We will be contacting you within the next 10-15 business days. Thank you for coming in." """)
    print
    wrap(""""Thank you for your time." You reply, shaking their hand. After you leave, your best friend calls you and asks if you want to grab dinner. You agree, and meet up at the local Mel's Diner later on that day.""")
    print
    pause = raw_input("Press ENTER to continue")
    os.system('cls' if os.name == 'nt' else 'clear')
    print
    wrap("""Mel's is packed at this time of night. People are coming in, after attending a happy hour elsewhere, looking for something greasy to soak up the alcohol coarsing through their systems. You find your friend, and you\'re both seated after about a 30 minute wait.""")
    print
    wrap("""You make small talk as you peruse the menu. It's been a while since you've seen your friend last, because school and finals have gotten in the way. Your server shows up and asks for your order. You've narrowed it down to the following two choices:""")
    for item in sit2Choices:
        print
        wrap(item)
        print
    choice = raw_input(">")
    process(choice)
    if choice == "1" and Toon == "Taylor Swift":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        wrap(""""A bit hungry are we? How would you like it cooked?" your server inquires, surprisedly.""")
        print
        wrap(""""Medium Rare, please" """)
        print
        wrap(""""Very well." """)
        print
        wrap(""" After taking your friend's order of a roasted chicken, your server leaves. Then your friend turns to you with a quizzical look, and says, "Steak? Are you no longer watching what you eat?" """)
        print
        wrap(""""Um, I don\'t know... I\'m just really hungry today, I guess." """)
        print
        wrap(""""OK, well as long as you are mindful of how often you eat like this. Once in a while is ok, but this is an unhealthy appetite to support." """)
        pause = raw_input("Press ENTER to continue.")
        str(pause)
        if pause == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            wrap("""Aghast at your friend\'s audacious judgement, you snatch your friend\'s weave, hold it in the air, drop the mic, and make your exit.""")
        end()
    if choice == "2" and Toon == "Taylor Swift":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        wrap(""""A salad? Nice, I wish I could get my wife to order one at dinner," remarks your friend.""")
        print
        wrap(""""Yeah, I always try to watch how much I eat, don\'t want to gain too much weight," you reply. """)
        print
        pause = raw_input("Press ENTER to continue.")
        end()
    if choice == "1" and Toon == "Chris Evans":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        wrap(""""And...how would you like it cooked?" your server asks.""")
        print
        wrap(""""Medium rare." """)
        print
        wrap(""""Yeah, man! Hookin? it up. I?ll get one myself, cooked the same way." """)
        print
        wrap(""""Well, this is what I always order. I love the way this place makes it. And you know I gotta keep my protein intake up." """)
        print
        wrap(""""Shouldn't be too hard with an appetite that healthy!" """)
        pause = raw_input("Press ENTER to continue.")
        end()
    if choice == "2" and Toon == "Chris Evans":
        os.system('cls' if os.name == 'nt' else 'clear')
        print
        wrap(""""Are you seriously having a salad? Are you sick or something? Or is that your appetizer?" """)
        print
        wrap(""""Nah, man. I\'ve just been trying to eat healthier lately." """)
        print
        wrap(""""That doesn't mean you have to starve yourself, though!" Your friend turns to your server and says, "I'll have the steak, medium rare," they turn back to face you, and playfully smirks, "for starters." """)
        pause = raw_input("Press ENTER to continue.")
        str(pause)
        if pause == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            wrap("""You swiftly punch your friend in their smug ass face, and walk away becasue cool guys don\'t look back""")
        end()

def end():
    os.system('cls' if os.name == 'nt' else 'clear')
    print
    wrap("""The rest of the dinner goes pretty smoothly. You're best friends, after all. After catching up for the next couple hours, you split the bill and part ways.""")
    print
    wrap("""On your way home you take some time to reflect on the day's events. You begin to wonder to yourself: "Would things have been different if I expressed a different gender?" """)
    print
    print """                       *     *     *"""
    print
    wrap("Do you want to play again? (y/n)")
    restart = raw_input(">")
    process(restart)
    if restart == "y" or "yes":
        os.system('cls' if os.name == 'nt' else 'clear')
        start()
    if restart == "n" or "no":
        sys.exit()


    
#Game starts here
os.system('cls' if os.name == 'nt' else 'clear')
start()
