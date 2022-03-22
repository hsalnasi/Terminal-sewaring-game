import random
import datetime

# intro banner
intro_msg = """ *********************** Welcome sucker ********************************* \n

 --------------------------------------------------------------------
 press a number to start . LOSER 
 --------------------------------\n
 1- I wanna learn new nasty words for some Educational Purposes . 
 2- let's fight ! 
 3- my name is Amir , please roast me ."""

# swear data
swearing_words = ["bastard", "bitch", "bitchy", "asshole",  "bullshit", "cockface", "damn", "fuckass",
                  "fucking", "fucker", "fucks", "hell", "jagoof", "jackass", "shit", "peice of shit!", "shitty"]
swearing_sen = ["oh yeah ? Maybe ur ugly ass ? ", "that's funny ! cuz as far as i'm seeing",
                "ur face could scare the shit out of a toilet .", "how long did it take you to come up with that one ? LMAO .", " ok u"]
amir_swords = ["Terrorist", "Ali express's Kakashi", "Jude", "Fake Badwi",
               "mr.emotions", "ali express's Emo boy .", "Nerd", "mr.Yamto is better than me"]
amir_sent = ["I almost can hear u cryin from here . stop it ",  "Why? is it beacuse of ur flat ass?",
             "maybe cuz you'll never get to hear my voice eilf ?", "STFU", "UMMM... ur MUM ?" , "Maybe when u man up " , "sure , sure .. but ur still a terroriest lmao"]
not_enough = ["not enough? ugh ",
              "WTF ! do u really like to curse ? lol ", "Get a life u swearing nerd"]


# prints a random set of 3 swear words from a list of swears. lets the user choose to prints more sets of swear words
def answer_1():
    while True:
        # generate three random indexes (possibly repeating)
        firstword_idx = random.randint(0, len(swearing_words) - 1)
        secondword_idx = random.randint(0, len(swearing_words) - 1)
        thirdword_idx = random.randint(0, len(swearing_words) - 1)

        # get random words using random indexes
        first_word = swearing_words[firstword_idx]
        second_word = swearing_words[secondword_idx]
        third_word = swearing_words[thirdword_idx]

        # print the message, along with the words inside
        print("You wanted to educate .. so Welcome to ur NASTY DICTIONARY")
        print("\n"*2)
        print(first_word)
        print(first_word + " " + second_word + " " + third_word)
        print("\n"*2)

        # prompt the user, and then break out of loop depending on answer
        fake_ask = input(" \n (press enter for more , and No to stop . ")

        if fake_ask == "no" or fake_ask == "NO":
            print("""\n \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n
            \nWaah I thought u were tough and ready to learn but I guess this is it""")
            break


# lets the user input anything. the program then replies with a random swear sentence, if the input is not no
def answer_2():
    # print starting banner
    firstword_idx = random.randint(0, len(swearing_words) - 1)
    first_word = swearing_words[firstword_idx]
    print("""<<<<<<<<-------------______________----------_____________------------->>>>>>\n
        LET THE BATTELE BEGIN U {} ! 
        ____________________________________\n \n""" . format(first_word))
    print("\n ***** press 'No' to quit the battele . ******")
    print()

    while True:
        # let the player write anything
        player_curse = input("type in ur curse here : \n")

        # if input is no, print winner msg and stop
        if player_curse.lower() == "no":
            dt = datetime.datetime.now()
            print(""" on {}  \n 
            let the world wittnes that this {} has got his ass beatin . AMEN . """.format(dt, first_word))
            break

        # print random curse
        reply_idx = random.randint(0, len(swearing_sen) - 1)
        reply = swearing_sen[reply_idx]
        print(reply)


#  i will repeat almost the same steps on answer_2 function . since this will also be a battle and a turn based function.
def answer_3():
    # im gonna make a banner , just a small line of roasting
    amir_banner = """A .... M ... I .... R .... WHO WILL NEVER MARRY Ahri .
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ 
    \n 
    Here we meet ..
    """

    print(amir_banner)

    # printing a statment before taking amir's input , just to let him know that he should go first .
    print("You can go first. it's gonna be fun to watch ")
    print("\n")
    print("press \"i cant't\" to quit")
    
    while True:
        # ask amir for input, check if he wants to quit
        amir_input = input()
        if amir_input.lower() == "i can't":
            print("Bye Bye  {}".format(random.choice(amir_swords)))
            break
        
        # print a random insult from amir_sent
        print(random.choice(amir_sent))


# print intro message
print(intro_msg)

# request user input for main menu options, consider adding error checks here
try :
    user_input = int(input())
except :
    print("R U BLIND ? WRITE A NUMBER ONLY")
    quit() 

if user_input == 1:
    answer_1()
elif user_input == 2:
    answer_2()
elif user_input == 3:
    answer_3()
else:
    print("R U BLIND ? WRITE A NUMBER IN MENU ONLY")
