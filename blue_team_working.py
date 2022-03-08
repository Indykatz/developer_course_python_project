# Code Nation: 
# Text based RPG football penalty game
# Blue Team: Michal, Ash, Katy, Antony

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

#-------------------------
# IMPORT LIBRARIES SECTION
#-------------------------

# Random library for generating items from list 
import random

# import time lib timing_print_func() and to slow the game down with time.sleep()
import time

# import system used in timing_print_func()
import sys

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# ---------------------------------
# VARIABLES TO BE USED ACROSS GAMES 
# ---------------------------------

# User name - used in user_info_func() function - never changed 
user_name_var = None 

# Games won - used to keep a score of the players games - adds 1 if players wins
games_won = 0

# Games lost - used to keep a score of the players games - adds 1 if player loses
games_lost = 0

# List of teams_list - used in player and comp selecting teams and road to cup intro
# Selected in pick_player_team_func() & pick_comp_team_func()
teams_list = ["England", "Italy", "France", "Germany",
"Spain", "Turkey", "Portugal", "Switzerland", "Denmark" , 
"Russia", "Wales", "Scotland", "Ireland", "Northern Ireland", 
"Netherlands", "Belgium", "Sweden","Poland", "Ukraine","Austria", 
"Slovakia", "Czech Republic", "Croatia", "Serbia"] 

# Players team - will equal a item from team list - used in the game - reset for each new game
# Declared in pick_player_team_func() 
player_team_var = None

# Comp Team - will equal a item from team list - used in the game - reset for each new game
# Declared in pick_comp_team_func() 
comp_team_var = None 

# First team - Used in show who won the coin toss and takes 1st penalty
# Decalred incoin_toss()
first_team_var = None 

# player score - keeps players score in a match - reset at new game
# the_game_func()
player_score_var = 0 

# Comp score - keeps players score in a match - reset at new game
# the_game_func()
comp_score_var = 0 

# penalty tries - the number of penalties - reset at new match
# the_game_func()
pen_tries_var = 0 

# dice roll direction list - used to pick event for goal or save
# the_game_func()
dice_roll_list = [1, 2, 3, 4, 5, 6] 

# dice roll repsonses - used for each dice roll
dice_line_var = ["He wont get this!", "This will be a goal", "He's got this", "He looks nervous"]

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

#--------------------
# Images used in game
# -------------------

# Left football image used in logo_func
ball_left_img = ("""
    __
 .'".'"'.        ---   ---   ---    
:._.""._.:           ---   ---
:  \__/  :      ---     ---
 './  \.'
    ""
    """)

# Right football img used in logo_func
ball_right_img = ("""
    
                        __
---   ---   ---      .'".'"'.  
   ---   ---  ---   :._.""._.:
---   ---   ---     :  \__/  :
                     './  \.'
                        ""
    """)

# Heads image for coin toss
heads_img = ("""    
                x  x
             x H H H x
            x H H H H x
            x H H H H x
             x H H H x
                x  x
    """)

# Tail image for coin toss
tails_img = ("""    
                x  x             
              x T T T x        
             x T T T T x      
             x T T T T x     
              x T T T x        
                x  x            
    """)

# Goal image 01 - used for goals
goal_image_1 = ("""\
                     ___
 o__        o__     |   |
/|          /\      |   |X
/ > o        <\     |   |XX
""")

# Goal image 02 - used for goals
goal_image_2 = ("""\
        \O                                     ,  .-.___
  -     /\                                   O/  /xx\XXX|
 -   __/\ `                                  /\  |xx|XXX|
    `    \, ()                              ` << |xx|XXX|
^^^^^^^^`^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """)

# Goal image 03 - used for goals
goal_image_3 = ("""\
    Ⓖ  Ⓞ  Ⓐ  Ⓛ  ! ! ! 
""")

# Miss image 01 - used for miss
miss_image_1 = ("""\
     _\|      __     |/_
   _-  \_   _/"->   _/  -_
   -_    `-'(   )`-'    _-
    `=.__.=-(   )-=.__.='
            |/-\|
            Y   Y
        """)

# Miss image 02 - used for miss
miss_image_2 = ("""\
                            ____
                   .---'- - -  
      .-----------/           |
     /           (         ^  |   __
&   (             \        O  /  / .'
'._/(              '-'  (.   (_.' /
     \                    \     ./
      |    |       |    |/ '._.'
       )   @).____\|  @ |
   .  /    /       (    | 
  \|, '_:::\  . ..  '_:::\ ..\).
        """)

# Miss image 03 - used for miss
miss_image_3 = ("""\
           ___
         .';:;'.
        /_' _' /\   __
        ;a/ e= J/-'"  '.
        \ ~_   (  -'  ( ;_ ,.
         L~"'_.    -.  \ ./  )
         ,'-' '-._  _;  )'   (
       .' .'   _.'")  \  \(  |
      /  (  .-'   __\{`', \  |
     / .'  /  _.-'   "  ; /  |
    / /    '-._'-,     / / \ (
 __/ (_    ,;' .-'    / /  /_'-._
`"-'` ~`  ccc.'   __.','     \j\Lj
                 .='/|\7      
                   ' `
        """)

# winner cup used for winner
winner_cup_img = ("""
              .-=========-.
              \'-=======-'/
              _|   .=.   |_
             ((|  {{1}}  |))
              \|   /|\   |/
               \__ '`' __/
                 _`) (`_
               _/_______\_
              /__________/,
""")

# UEFA cup used at road to cup 
uefa_cup_img = ("""\
                         ___________
                        '._==_==_=_.'
                        .-\:      /-.
                       | (|:.     |) |
                        '-|:.     |-'
                          \::.    /
                           '::. .'
                             ) (
                           _.' '._
                          `-------`
""")


# used at team list
euro_img = ('''\
            
             ,adPPYba, 88       88 8b,dPPYba,  ,adPPYba,   
            a8P_____88 88       88 88P'   "Y8 a8"     "8a  
            8PP""""""" 88       88 88         8b       d8  
            "8b,   ,aa "8a,   ,a88 88         "8a,   ,a8"  
            `"Ybbd8"'  `"YbbdP'Y8 88          `"YbbdP"'   

 ''')
 # dice image ('r' prints raw)
dice_img = (r"""
   _______
  /\ o o o\
 /o \ o o o\_______
<    >------>   o /|
 \ o/  o   /_____/o|
  \/______/     |oo|
        |   o   |o/
        |_______|/
 """)
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# --------------------------
# List to be used as randoms
# --------------------------

"""
    This section is for our lists used in the game
"""

# used when saved a goal
save_list = ["THIS GOALIE IS AMAZING\n\n", "WHAT A SAVE\n\n"]

# used as diections to go select from list
directions_list=["Top Left", "Top Middle", "Top Right",
"Left", "Middle", "Right",
"Bottom Left", "Bottom Middle", "Bottom Right"]

# a list of goal images to be used randomly 
goal_image_list = [goal_image_1, goal_image_2, goal_image_3]

# a list of goal statements used with pictures list 
goal_statement_list = [
"GOAL!!!\n\nWHAT A FINISH\n\n", 
"GOAL!!!\n\nHE SMASHED IT IN\n\n",
"GOAL!!!\n\nBACK OF THE NET\n\n",
"GOAL!!!\n\nIT'S A CLEAN SHOT THE GOALIE MIGHT HAVE TROUBLE WITH THIS ONE\n\n", 
"GOAL!!!\n\nHE SHOOTS, HE SCORES, THE CROWD GOES WILD\n\n"]

# a list of miss statements to be used randomly 
miss_statement_list = ["MISSED PENALTY!!!!!!!!\n\nHE SHOOTS AND MISSES!\n\n",
"MISSED PENALTY!!!!!!!!\n\nWHAT A SUPER SAVE!\n\n",
"MISSED PENALTY!!!!!!!!\n\nCHOW DID HE STOP THAT!\n\n", 
"MISSED PENALTY!!!!!!!!\n\nCOMPLETELY MISSED THE BALL! EPIC FAIL\n\n"]

# a list of fail images to be used randomly 
fails_image_list = [miss_image_1, miss_image_2, miss_image_3]

# a list of fail images to be used with picture 
fail_statment_list = [
"An eagle swoops in scratches the ref in the eye. Would you believe it he flys off with the ball!\n\n", 
"An elephant finds its way on to the pitch and pops the ball injuring a few players and destroying the feild.\n\n", 
"Golem from lord of the rings claims the ball as his precious\n\n"]

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -----------------------------------------
# Michal Ash Katy Antony logo_func function
# -----------------------------------------

""" 
    Used in intro_func() method to introduce the game
    uses print statements to create logo
"""

def logo_func():
    print("---------------------------------------")
    print(ball_left_img)
    print("          PENALTY SHOOT OUT            ")
    print("                  BY                   ")
    print("              MAKA GAMES               ")
    print(ball_right_img)
    print("---------------------------------------")

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# ----------
# Time print
#-----------
"""
    prints out strings character by character

    for each letter in a sentance 
    print letter, wait, next letter, wait 
    repeat till done

"""
def printing_time(a_string):
    for character in a_string:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -------------------------
# User information function
# -------------------------
""" 
    Used in intro_func() method to get players name

    user input gets user name
    prints using our printing_time_func()
"""

def user_info_func():
    global user_name_var
    user_name_var = input("Please enter your name ... ").capitalize() 
    printing_time(f"\nWelcome {user_name_var}! You are now playing in the SEMIFINALS of the UEFA Euro 2024\n\n")
    time.sleep(0.8)
    input("PRESS ENTER TO CONTINUE\n")

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -------------------------
# User Information function
# -------------------------
"""
    Used to display players results of all games.
    Used at starts of new games

    Prints user game history information
"""

def user_history_func():
    print(f"Player: {user_name_var}\n\nGames Won: {games_won}\n\nGames Lost: {games_lost}\n\nTotal Games: {(games_won+games_lost)}\n")
    time.sleep(0.2)
    input("PRESS ENTER TO CONTINUE\n")

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -----------------------
# List Generator function 
# -----------------------
""" 
    This function generates numbered lists for the games lists
    example:
    1. item
    2. things

    Function is called throughout game to generate numbered lists
"""

def gen_list_func(a_list):
    teams_list # use the list of teams used in the game
    global directions_list # use the list of directions used in the game
    number_in_list = 1 # start list at number 1
    for each_item in a_list: # for each item in the list 
        print(f"{number_in_list}. {each_item}") # print the number and item
        time.sleep(0.2) # wait
        number_in_list +=1 # add 1 to the list
        # repeat until all items in list have been printed with numbers

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# --------------------------------------------------
# Picking PLAYER team with and handling a ValueError
# --------------------------------------------------

"""
    picking player team from team_list
    Uses our list gen function to generate teams lists
    uses user input for selection 

    While True exception error handling 
    loops over and over until correct value is inputted i.e. 1-n
"""

def pick_player_team_func():
    global player_team_var
    global user_name_var
    global teams_list

    print(euro_img)

    print("GETTING TEAMS\n")
    time.sleep(0.1)

    teams_list.sort()
    gen_list_func(teams_list)

    while True:
        try:
            pick_team_var = int(input(f"\nPlease select PLAYER National Team from the list: (1-24) "))
            if pick_team_var in range(1, len(teams_list)+1):
                pick_team_var -= 1 
                player_team_var = teams_list[pick_team_var]
                teams_list.remove(player_team_var)
                printing_time(f"\n{user_name_var} selected to play as {player_team_var}\n\n")
                time.sleep(0.8)
                input("PRESS ENTER FOR COMPUTER TO SELECT TEAM\n")
                break
        except:
            print(f"\nThat's not a valid option\n")
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

#-------------------------
# Comp picks team randomly
# ------------------------

"""
    Picks a team for comp randomly

    Using random lib
"""
def pick_comp_team_func():
    global teams_list
    global comp_team_var
    comp_team_var = random.choice(teams_list)
    printing_time(f"Computer picked to play as {comp_team_var}\n\n")
    teams_list.remove(comp_team_var)
    time.sleep(0.8)
    input(f"\nPRESS ENTER TO SET GAME UP\n")
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# --------------------------
# Game introduction function
# --------------------------

"""
    Road to cup
    creates new list of 7 random teams from team list
    These teams are used in the back story

    Road to cup is over view of how team got to semis
"""

def game_intro_func():
    round_up_list = []
    for i in range(0, 8):
        round_up_list.append(random.choice(teams_list))


    print(uefa_cup_img)

    printing_time("--- --- --- --- WELCOME TO UEFA EURO 2024 SEMIFINALS --- --- --- ---\n\n")

    printing_time(f"{player_team_var} WAS DRAWN IN GROUP C ALONGSIDE {round_up_list[0]}, {round_up_list[1]} AND {round_up_list[2]}\n\n")


    printing_time(f"In first match {player_team_var} drew with {round_up_list[1]} by one goal each.\n\nThe next two games against {round_up_list[2]} and {round_up_list[0]} ended both 2:0 to {player_team_var}.\n\nThis means {player_team_var} went on to win the GROUP C with 7 points and met {round_up_list[3]} in the ROUND OF 16.\n\n")

    printing_time(f"After a very good start to the game as the favourites, {player_team_var} scored from a free kick in 20th minute.\n\nIn second half no goals were scored, even when {round_up_list[3]} hit the crossbar from very last desperate attempt.\n\n")

    printing_time(f"In QUARTERFINALS {player_team_var} wins against {round_up_list[4]}.\n\nThe match started very slow, it reminded us more of chess game. \n\nFirst half draw was an expected result. Second half went underway and not even 5 minutes in {round_up_list[4]} scored from counter attack. 1:0!\n\n{player_team_var} had to make changes quickly and after a double substitution they managed to equalise in 68th minutes. 1:1!\n\nBoth team then started a competition of missed chances so the match went had to go into overtime.\n\nBefore the second half of overtime, the manager of {player_team_var} made a final substitution and MY DEAR IT PAYED OFF !!\n\n6 minutes to go he received the ball at the edge of the box and smashed it into the top corner.\n\nThat was a rocket. 2:1! {player_team_var} is in SEMIFINALS !!!\n\n")
    
    printing_time(f"SEMIFINALS against the favourites of whole tournament {comp_team_var} was expected to be a hard game.\n\nThey beat {round_up_list[5]} in Round 16 by 3 goals to 1.\n\nThey went on to beat a very strong Team {round_up_list[6]} 2:0 in the QUARTERFINALS.\n\nStrong Teams, experienced managers, world class players. What else do you want?!\n\nThe match started and both teams went right at it. One tackle after another, deep pressing. Very good game!\n\nIn the 27th minute {comp_team_var} strikes first. 1:0!\n\n{player_team_var} started to push forward more and more but no success. First half score was 1:0 for {comp_team_var}\n\n")
    
    printing_time(f"Second half started with huge pressure from {player_team_var}, Attack after attack but couldn't score a goal.\n\n{player_team_var} missed two clear cut chances.\n\nIt was nearly over when the substitute player received a ball in the middle of the field\n\nHe ran passed players and scored from outside the box with a blast from his right foot in 88th minute.\n\n1:1!\n\nOVERTIME was very cagey yet they still managed to miss an open goal from 8 yards out. PENALTIES!!!\n\n")
    
    printing_time(f"WHOLE OF EUROPE IS WATCHING.\n\nTHERE IS HOPE!\n\nTHERE IS QUALITY!\n\nIF NOT NOW WHEN?!\n\n")
    
    printing_time(f"ALL EYES ON YOU!\n\nTHE CROWD IS SHOUTING YOUR NAME!\n\nARE YOU CONFIDENT ENOUGH TO TAKE THAT RESPONSIBILITY AND SEND YOUR COUNTRY TO EUFA EURO 2024 FINAL?\n\n")
    time.sleep(0.8)
    input(f"PRESS ENTER TO CONTINUE\n")

# -----------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------- 

# -----------------------------------------    
# Coin Toss - who goes first player or comp
# -----------------------------------------

"""
    Randomly selects heads or tails 
    Heads Player goes first
    Tails comp goes first
    Sets global variable first_team_var to show the game who takes the first penalty each turn

    uses random lib
"""

def coin_toss_func():
    # Use games variables which are used in other functions: 
    global first_team_var

    # Coin Toss local varible as only used in this function
    coin_toss_var = ["Heads", "Tails"]

    printing_time("The coin toss will determain who goes first PLAYER or COMPUTER.\n\n")
    printing_time("Heads player goes first, Tails computer goes first.\n\n")
    input("PRESS ENTER TO CONTINUE\n")
    coin_roll_var = random.choice(coin_toss_var)
    print(f"Coin lands on {coin_roll_var}\n\n")
    # Head
    if coin_roll_var == "Heads":
        print(heads_img) # heads image
        first_team_var = player_team_var
    # Tails
    if coin_roll_var == "Tails":
        print(tails_img) # tails image
        first_team_var = comp_team_var

    print("-------------------------------------------")
    printing_time(f"{first_team_var} will take the first penalty\n\n")
    time.sleep(0.8)
    input("PRESS ENTER TO CONTINUE\n")    
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# ----------------------------------
# Playing the game in turns function
# ----------------------------------

"""
    Plays the game depending on who goes first player or comp
    Makes the game play in turns while checking it doesnt go over 5 penalties
"""

def the_game_func():
    global pen_tries_var

    while pen_tries_var < 5:
        pen_tries_var += 1
        printing_time(f"Round {pen_tries_var} of penalties\n\n")
        if first_team_var == player_team_var:
            player_go_func() # calls player_go_fun()
            comp_go_func() # Calls comp_go_func()
            the_game_func() # repeat

        if first_team_var == comp_team_var:            
            comp_go_func() # comp go 
            player_go_func() # player go 
            the_game_func() # repeat

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -------------------
# PLAYERS GO FUNCTION
# -------------------

"""
    Player to take penalty via dice roll
    if dice = 6 - goal 
    if dice = 3 - question
    if dice = 1 - miss
    if dice = 2 or 4 - chance at direction
""" 

def player_go_func():
    global player_score_var # SET AS GLOBAL AS WILL BE AMENDED
    directions_list
    save_list

    printing_time(f"{player_team_var} steps up to score a penalty\n\n")
    time.sleep(0.5)

    printing_time(random.choice(dice_line_var))
    dice_roll_var = random.choice(dice_roll_list)
    printing_time(f"\n\nTHE ROLL IS \n\n ... ")
    time.sleep(1)
    print(dice_img)
    print(f"{dice_roll_var}\n")

    # if dice equal 6 
    if dice_roll_var == 6:
        printing_time("OVERRIDE YOU SCORE A PENALTY\n\n")
        player_score_var += 1
        goal_func()
        
        printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n\n")
        time.sleep(0.8)
        input("PRESS ENTER TO CONTINUE\n")

    # if dice equal 1 
    if dice_roll_var == 1:
        print("\nOVERRIDE YOU MISS A PENALTY\n")
        fails_func()
        printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n\n")
        time.sleep(0.8)
        input("PRESS ENTER TO CONTINUE\n\n")

    # if dice equals 3 or 4 
    if dice_roll_var == 3 or dice_roll_var == 4:
        print("\nOVERRIDE YOU MUST ANSWER A QUESTION TO SCORE\n\n")
        random_question_gen_func()
        printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n\n")
        time.sleep(0.8)
        input("PRESS ENTER TO CONTINUE\n\n")

    # if dice equals 2 or 5 
    # if dice_roll_var = 2 or dice_roll_var = 5 (replace line below with this)
    if dice_roll_var > 1 and dice_roll_var < 6 and dice_roll_var != 3 and dice_roll_var != 4:
        printing_time("WHICH WAY WILL HE GO\n\n")
        gen_list_func(directions_list)
        while True:
            try:
                player_direction_int = int(input(f"\nPlease select direction to score ...")) 
                if player_direction_int in range(1, len(directions_list)+ 1):
                    player_direction_int -= 1 
                    player_direction = directions_list[player_direction_int]
                    com_direction = random.choice(directions_list)
                    print(f"\n{player_team_var} went {player_direction}, {comp_team_var} went {com_direction}\n")
                    break
            except:
                print("That's not a valid option")

        if player_direction != com_direction:
            goal_func()
            player_score_var += 1
            printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n")
            time.sleep(0.8)
            input("PRESS ENTER TO CONTINUE\n")
        if player_direction == com_direction:
            miss_func()
            printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n\n")
            time.sleep(0.8)
            input("PRESS ENTER TO CONTINUE\n")
            
            
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -------------------
# COMP GO FUNCTION
# -------------------

"""
    Comp to take penalty vai dice roll
    if dice = 6 - miss 
    if dice = 1 - goal
    if dice = 2, 3, 4 - chance at direction
""" 

def comp_go_func():
    global comp_score_var

    printing_time(f"{comp_team_var} steps up to shoot a penalty\n\n")

    printing_time(random.choice(dice_line_var))
    dice_roll_var = random.choice(dice_roll_list)
    printing_time(f"\n\nTHE ROLL IS \n\n ... ")
    time.sleep(1)
    print(dice_img)
    print(f"{dice_roll_var}\n")


    if dice_roll_var == 6:
        printing_time("\nOVERRIDE YOU SCORE A PENALTY\n\n")
        goal_func()
        comp_score_var += 1
        printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n\n")
        time.sleep(0.8)
        input("PRESS ENTER TO CONTINUE\n\n")

    if dice_roll_var == 1:
        printing_time("\nOVERRIDE YOU MISSED A PENALTY\n\n")
        fails_func()
        printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n\n")
        time.sleep(0.8)
        input("PRESS ENTER TO CONTINUE\n\n")

    
    if dice_roll_var > 1 and dice_roll_var < 6:
        while True:
            printing_time("WHICH WAY WILL HE GO\n\n")
            gen_list_func(directions_list)  
            try:
                player_direction_int = int(input(f"\nPlease select direction to save ... \n"))
                if player_direction_int in range(1, len(directions_list)+ 1):
                    player_direction_int -= 1
                    player_direction = directions_list[player_direction_int]
                    com_direction = random.choice(directions_list)
                    printing_time(f"{player_team_var} went {player_direction}, {comp_team_var} went {com_direction}\n\n")
                    break
            except:
                print(f"\nThat's not a valid option\n")

        if player_direction != com_direction:
                goal_func()
                comp_score_var += 1
                printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n\n")
                time.sleep(0.8)
                input("PRESS ENTER TO CONTINUE\n\n")

        if player_direction == com_direction:
            miss_func()
            printing_time(f"Score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n\n")
            time.sleep(0.8)
            input("PRESS ENTER TO CONTINUE\n\n")


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -----------------------
# goals misses and fails
# -----------------------

"""
    Used in players and comps go to call statements and pictures (see picture section)

    these functions are called in player_go and comp_go 
    Will be called depended on if player/comp score, missses or fails
"""

def goal_func():
    print(random.choice(goal_image_list))
    printing_time(random.choice(goal_statement_list))

def miss_func():
    printing_time(random.choice(miss_statement_list))

def fails_func():
    num = random.randint(0,2)
    print(fails_image_list[num])
    printing_time(fail_statment_list[num])

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -----------
# final score
# -----------

"""
    This functions starts when both team have taken 5 penalties
    Uses global variable games_won and games_lost to keep score of players progress
    If draw calls sudden_death_func()
""" 

def final_score_func():
    global games_won
    global games_lost
    # print final penalty score
    printing_time(f"Final score is {player_team_var} {player_score_var} : {comp_team_var} {comp_score_var}\n")
    if player_score_var == comp_score_var and pen_tries_var != 0:
        time.sleep(0.8)
        printing_time("SUDDEN DEATH MATCH\n\n")
        sudden_death()
    elif player_score_var > comp_score_var:
        games_won =+ 1
        print(winner_cup_img)
    elif player_score_var < comp_score_var:
        games_lost =+ 1
    start_again_func()

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# ---------------
# RANDOM QUESTION
# ---------------
"""
    Random question is used in sudden death and in if player rolls a 3 for a chance
"""
def random_question_gen_func():
    global player_score_var
    random_answer_1 = "Brazil"
    random_answer_list_1 = ["Brazil", "Italy", "France"]
    random_answer_2 = "M. Owen"
    random_answer_list_2 = ["Ronaldo", "Z. Zidane", "M. Owen"]
    random_answer_3 = "H. Kane"
    random_answer_list_3 = ["R. Sterling", "H. Kane", "M. Rashford"]
    random_answer_4 = "1958"
    random_answer_list_4 = ["1955", "1958", "1960"]
    random_answer_5 = "Italy"
    random_answer_list_5 = ["Englad", "Italy", "Spain"]
    random_answer_6 = "Wayne Rooney"
    random_answer_list_6 = ["Wayne Rooney", "Booby Charlton", "Gary Lineker"]
    random_answer_7 = "Miroslav Klose"
    random_answer_list_7 = ["Ronaldo Nazario", "Pele", "Miroslav Klose"]
    random_answer_8 = "Dani Alves"
    random_answer_list_8 = ["Dani Alves", "Kenny Dalglish", "Andres Iniesta"]
    sd_question_list = ["Which country won the highest number of world cups?",
    "In 2001 who was the European footballer of the year?",
    "which England player won the golden boot award in FIFA 2018?",
    "In which year UEFA EURO was played for first time?",
    "Who won the last European Championships?",
    "Who is the England's all time top scorer",
    "Who is the World Cup all time top goal scorer?",
    "Who won THE MOST MAJOR trophies as a player?",
    ]

    random_question = random.choice(sd_question_list)
    print(f"{random_question}\n")
    random_q_index = sd_question_list.index(random_question)
    if random_q_index == 0:
        gen_list_func(random_answer_list_1)    
        while True:
            try:
                user_guess_var = int(input("\nplease enter answer by number ... \n"))
                if user_guess_var in range(1, len(random_answer_list_1)+1):
                    user_guess_var -= 1
                    if random_answer_1 == random_answer_list_1[user_guess_var]:
                        player_score_var += 1
                        printing_time("SCORE.\n\n")
                        break
                    if random_answer_1 != random_answer_list_1[user_guess_var]:
                        printing_time("MISS\n\n")
            except:
                print("That is not a valid option")
    if random_q_index == 1:
        gen_list_func(random_answer_list_2)
        while True:
            try:
                user_guess_var = int(input("\nplease enter answer by number ... \n"))
                if user_guess_var in range(1, len(random_answer_list_2)+1):
                    user_guess_var -= 1
                    if random_answer_2 == random_answer_list_2[user_guess_var]:
                        player_score_var += 1
                        printing_time("SCORE\n\n")
                        break
                    if random_answer_2 != random_answer_list_2[user_guess_var]:
                        printing_time("MISS\n\n")
                        break
            except:
                print("That is not a valid option")

    if random_q_index == 2:
        gen_list_func(random_answer_list_3)
        while True:
            try:
                user_guess_var = int(input("\nplease enter answer by number ... \n"))
                if user_guess_var in range(1, len(random_answer_list_3)+1):
                    user_guess_var -= 1
                    if random_answer_3 == random_answer_list_3[user_guess_var]:
                        player_score_var += 1
                        printing_time(f"\nSCORE\n\n\n")
                        break
                    if random_answer_3 != random_answer_list_3[user_guess_var]:
                        printing_time(f"\nMISS\n\n")
                        break
            except:
                print("That's not a valid option")

    if random_q_index == 3:
        gen_list_func(random_answer_list_4)
        while True:
            try:
                user_guess_var = int(input("\nplease enter answer by number ... \n"))
                if user_guess_var in range(1, len(random_answer_list_4)+1):
                    user_guess_var -= 1
                    if random_answer_4 == random_answer_list_4[user_guess_var]:
                        player_score_var += 1
                        printing_time(f"\nSCORE\n\n")
                        break
                    if random_answer_4 != random_answer_list_4[user_guess_var]:
                        printing_time(f"\nMISS\n\n")
                        break
            except:
                print("That's not a valid option")
    if random_q_index == 4:
        gen_list_func(random_answer_list_5)
        while True:
            try:
                user_guess_var = int(input("\nplease enter answer by number ... \n"))
                if user_guess_var in range(1, len(random_answer_list_5)+1):
                    user_guess_var -= 1
                    if random_answer_5 == random_answer_list_5[user_guess_var]:
                        player_score_var += 1
                        printing_time(f"\nSCORE.\n\n")
                        break
                    if random_answer_5!= random_answer_list_5[user_guess_var]:
                        printing_time("\nMISS\n\n")
                        break
            except:
                print("That's not a valid option")        
    if random_q_index == 5:
        gen_list_func(random_answer_list_6)
        while True:
            try:
                user_guess_var = int(input("\nplease enter answer by number ... \n"))
                if user_guess_var in range(1, len(random_answer_list_6)+1):
                    user_guess_var -= 1
                    if random_answer_6 == random_answer_list_6[user_guess_var]:
                        player_score_var += 1
                        printing_time(f"\nSCORE\n\n")
                        break
                    if random_answer_6!= random_answer_list_6[user_guess_var]:
                        printing_time(f"\nMISS\n")
                        break
            except:
                print(f"\nThat's not a valid option\n")    

    if random_q_index == 6:
        gen_list_func(random_answer_list_7)
        while True:
            try:
                user_guess_var = int(input("\nplease enter answer by number ... \n"))
                if user_guess_var in range(1, len(random_answer_list_7)+1):
                    user_guess_var -= 1
                    if random_answer_7 == random_answer_list_7[user_guess_var]:
                        player_score_var += 1
                        printing_time(f"\nSCORE\n\n")
                        break
                    if random_answer_7!= random_answer_list_7[user_guess_var]:
                        printing_time(f"\nMISS\n\n")
                        break
            except:
                print(f"\nThat's not a valid option\n")

    if random_q_index == 7:
        gen_list_func(random_answer_list_8)
        while True:
            try:
                user_guess_var = int(input("\nplease enter answer by number ... \n"))
                if user_guess_var in range(1, len(random_answer_list_8)+1):
                    user_guess_var -= 1
                    if random_answer_8 == random_answer_list_8[user_guess_var]:
                        player_score_var += 1
                        printing_time("\nSCORE\n\nn")
                        break
                    if random_answer_8!= random_answer_list_8[user_guess_var]:
                        printing_time("\nMISS\n\n")
                        break
            except:
                print(f"\nThat's not a valid option\n")                                    

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -----------------
# SUDDEN DEATH SHOT
# -----------------

"""
    Is called if draw. Allows one more penalty by question
    win or lose
"""

def sudden_death():
    global games_won
    global games_lost

    random_question_gen_func()
    if player_score_var > comp_score_var:
        printing_time("Great answer You scored and won this match in sudden death.\n\n")
        print(winner_cup_img)
        games_won += 1
        start_again_func()
    else:
        printing_time("Unlucky You missed and lost this match in sudden death.\n\n")
        games_lost -= 1
        start_again_func()

# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# -----------
# Start again
# -----------

"""
    Is called at the end of the final_score_funct() and sudden_death() functions
    Uses global varibales to keep track of players progress 
    resets games variables for next game
"""

def start_again_func():
    global player_score_var
    global comp_score_var
    global pen_tries_var
    play_again_var = input("Would you like to play again? type yes\n")
    if play_again_var == "yes":
        player_score_var = 0
        comp_score_var = 0
        pen_tries_var = 0
        play_game_func()
    else:
        printing_time(f"\nThanks for playing")
# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# ----------------
# PLAYING THE GAME
# ----------------

"""
    Using functions to set the game play
    Intro and Username in one function to start game and get user name
    The game play function is what is repeated at the start of each game 
    The whole game function allows the function to run from one line of code and in two sections 
"""

# Intro function and set user name
def intro_func():
    logo_func() # calls losgo  function which add our logo into game
    user_info_func() # calls user info function which allows user name into game
 
# play game function
def play_game_func():
    user_history_func() # calls user history function which allows user name into game
    pick_player_team_func() # calls pick player team function which allows user to select team
    pick_comp_team_func() # calls pick comp team function which allows user to select team
    game_intro_func() # calls the game intro function which introduces the game
    coin_toss_func() # calls the toss coin function which sets who goes first 
    the_game_func() # calls plays the game function which calls function within
    final_score_func() # calls the final score and end of game - restart can go here
    start_again_func() # calls start again function which gives player option to play again

def whole_game_func():
    intro_func() # call intro function
    play_game_func() # calls play game function


# -----------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------

# ----------------
# RUNNING THE GAME
# ----------------

"""
    The one line of code to run them all
    One line of code to bind them
"""

# Run game
whole_game_func() # calls the play_gamefunc() function which runs all functions to play the game

