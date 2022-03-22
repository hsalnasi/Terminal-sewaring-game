import random
import datetime

# should made the intro into a variable to make it imutable and work with functions.
#should made a pseduecode in the begining . 

print(""" *********************** Welcome sucker ********************************* \n

 --------------------------------------------------------------------
 press a number to start . LOSER 
 --------------------------------\n
 1- I wanna learn new nasty words for some Educational Purposes . 
 2- let's fight ! 
 3- my name is Hammar , please roast me .""" )
 # same variable mistake here . but nothing wrong in placing the input() after the print .
user_input = int(input())

################################################################
# good job here . if only made a pseduecode ... 
swearing_words = ["bastard" , "bitch" , "bitchy" , "asshole" ,  "bullshit" , "cockface" , "damn" , "fuckass" , "fucking" , "fucker" , "fucks" , "hell" , "jagoof" , "jackass" , "shit" , "peice of shit!" , "shitty"]
swearing_sen = [  "oh yeah ? Maybe ur ugly ass ? " , "that's funny ! cuz as far as i'm seeing , ur face could scare the shit out of a toilet ." , "how long did it take you to come up with that one ? LMAO ." , " ok u"]
amir_swords = ["Terrorist" , "Ali express's Kakashi" , "Jude" ,"Fake Badwi" , "mr.emotions" , "ali express's Emo boy ." , "Nerd" , "mr.Yamto is better than me"]
amir_sent  = ["I almost can hear u cryin from here . stop it " ,  "Why? is it beacuse of ur flat ass?"  ]
not_enough = ["not enough? ugh " , "WTF ! do u really like to curse ? lol " , "Get a life u swearing nerd"]
#########################################################################
#oh well ....

def answer_1 ():
    # shouldn't made the check inside of the function in the first place
    #cuz it's repitive . 
    if int(user_input) == 1 :
        # lack of logic and planing .. again . should've decided on one loop \while or for .
     for word in swearing_words:k

        while word in swearing_words:
         word_tuple = tuple(swearing_words)
         word_random = random.choices(word_tuple ,  k = len(swearing_words))
         print( "You wanted to educate .. so Welcome to ur NASTY DICTIONARY \n \n" , *word_random[:1] , ".\n" , *word_random[:3] , "\n")
         more_inpu = input(" \n (press enter for more , and No to stop . " )
         while more_inpu  :
             if more_inpu == "No" or "no"  :
              print( """\n \n ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n
           \nWaah I thought u were tough and ready to learn but I guess this is it {} """.format(*tuple(random.choice(swearing_words))))
              print("\nYOU'RE NOT COMING OUT OF THIS HELL ")
             break

           

         else:
                 print(*word_random[:-4] , *tuple(random.choices(word_random) , k = (word_random[1]) ))
                 print("=============================================")
                 print(*tuple(random.choice(not_enough)))

if (user_input) == 1 :
     print(  answer_1()  )
else :
    pass
               
             
        
# indentation party LMAO 

         


      

 
#################

# here i suppose to make it a turn based function where the player would write a sentence and i'll reply back to it with a random curse from my list .
randomm = tuple(random.choice(swearing_words))
def answer_2 () :
    if int(user_input) == 2 :
        print("""<<<<<<<<-------------______________----------_____________------------->>>>>>\n
        LET THE BATTELE BEGIN U {} ! 
        ____________________________________\n \n""" . format(randomm)) 
    else :
        pass

print("\n ***** press 'No' to quit the battele . ******")
player_curse = input("\n type in ur first curse here : \n")

random_player = tuple(random.choice(swearing_sen))
dt = datetime.datetime.now()
for player_curse in player_curse :
    count = 0
    while type(player_curse) == str or int :
        print(player_curse)
        print(random_player)
        count+=1
        if count == len(swearing_sen):
         if player_curse == "No".upper().lower().title() :

          print(""" on ({}) . \n 
        let the world wittnes that this {} has got his ass beatin . AMEN . """.format(dt , *tuple(random.choice(swearing_word)) )
     











   



    


 



         







