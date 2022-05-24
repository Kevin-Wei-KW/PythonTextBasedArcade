from random import *

money = 20
def rps():
    global money
    earned = 0
    wins = 0
    losses = 0
    rpc = ["r", "p", "s"]
    out = ["rock", "paper", "scissors"]
    opp = ["(-_-)", "(^___^)", "(@_@)"]
    print("Welcome to Rock Paper Scissors, type exit to leave")
    oppo = opp[randint(0,2)]
    print("Your opponent is...." + oppo)
    mode = input("Which game mode would you like to play, casual or competitive?")
    if mode.lower() == "casual":
        print("Let's play, what is your choice? Type r for rock, s for scissors, and p for paper")
        p = input ("\nWhat is your choice: ")
        while p.lower() != "exit" and money > 0:
            comp = randint(0, 2)
            print(oppo + ": "+out[comp] + " VS You[" + p + "]")
            if p.lower() == "exit":
                print("Thanks for playing rock paper scissors\nYou earned: " + str(earned))
                break
            if rpc[comp] == p:
                print("TIE!")

            elif (rpc[comp] == "r" and p == "p") or (rpc[comp] == "p" and p == "s") or (rpc[comp] == "s" and p == "r"):
                print("WIN! +3!")
                money += 3
                earned += 3
            elif (rpc[comp] == "p" and p == "r") or (rpc[comp] == "s" and p == "p") or (rpc[comp] == "r" and p == "s"):
                print("LOSE! -3!")
                money -= 3
                earned -= 3
            else:
                print("You cheated!\n-1!")
                money-=1
                earned -=1
            p = input("Again?: ")
    elif mode.lower() == "competitive":
        print("Let's play, what is your choice? Type r for rock, s for scissors, and p for paper")
        p = input("\nWhat is your choice: ")
        while p.lower() != "exit" and money > 0:
            comp = randint(0, 2)
            print(oppo + ": " + out[comp] + " VS You[" + p + "]")
            if p.lower() == "exit":
                print("Thanks for playing rock paper scissors\nYou earned: " + str(earned))
                break
            if rpc[comp] == p:
                print("TIE!")

            elif (rpc[comp] == "r" and p == "p") or (rpc[comp] == "p" and p == "s") or (rpc[comp] == "s" and p == "r"):
                wins += 1
                print("WIN!" + str(wins) + ":" + str(losses))

            elif (rpc[comp] == "p" and p == "r") or (rpc[comp] == "s" and p == "p") or (rpc[comp] == "r" and p == "s"):
                losses += 1
                print("LOSE!" + str(wins) + ":" + str(losses))

            else:
                print("You cheated!\n$-1!")
                money -= 1
                earned -= 1
            if wins == 3:
                money+=10
                earned+=10
                print("YAY, YOU WON! $+10")
                break
            if losses == 3:
                money-=10
                earned -=10
                print("YAY...wait, NOO, YOU LOST! $-10")
                break
            p = input("Again?: ")
    elif mode.lower() == "exit":
        return
    else:
        print("TYPO")
        exit(rps())

    print("earned: " + str(earned))
def hangman():
    global money
    print()
    print("Welcome to Clueless hangman! A letter guess takes 1 attempt, A word guess take 2 attempts!\nCategory: animals")
    #add more words into word bank with "" around it to expand game
    wordbank = ["dolphin", "dog", "tiger", "lion", "shark", "whale", "monkey", "rhinoceros", "hippopotamus", "giraffe", "eagle"]
    comp = wordbank[randint(0, len(wordbank)-1)]
    attempts = len(comp) + 3
    done = False
    out = []
    tostr = ""
    for i in range(len(comp)):
        out.insert(i, "_")
    print(out)
    while not done:
        if attempts < 1:
            print("LOST! -6")
            print("Answer: " + comp)
            break
        p = input("Your choice: ")
        print()

        if len(p) > 1:
            if p == comp:
                print("WIN! +10")
                money += 10
                break
            else:
                attempts-=2
                print("Attempts: " + str(attempts))
                continue
        else:
            attempts -= 1
            for i in range (len(comp)):
                if comp[i] == p:
                    out[i] = comp[i]
                elif out[i] == "_":
                    continue
            print(out)
            print("Attempts: " + str(attempts))
            if tostr.join(out) == comp:
                print("WIN! +10")
                money+=10
                break

def lottery():
    global money
    print("Are you here to go bankru.. *COUGH* EARN some money? You have come to the right place!")
    p = input("There is only one game here....wheel of fortune! \nGame is simple, 5$ to spin, you can get many different prizes, or lose money..Have fun! \nType: spin  to spin, exit to leave\n")
    prizes = [50, -20, 100000, -70, -15, "What do you call Santa's brothers and sisters?\nRelative clauses! comedy", 30, "If you got this, I hope you have a wonderful day!"]

    while (p.lower() != "exit" or p.lower() == "spin") and money >0:
        picked = prizes[randint(0,7)]
        if isinstance(picked, int):
            if picked >= 0:
                print("Congratz! You won " + str(picked) + " dollars!")
                money += picked
            else:
                print("RIP! You lost " + str(picked) + " dollars!")
        else:
            print(picked + " :)")

        p = input("Again?: ")
    print("Don't gooo, my money.....A bientot")

def jokes():
    list = ["What do you call Santa’s brothers and sisters? Relative clauses.", "The past, the present and the future all walked into a bar. It was tense.", "What’s the difference between a cat and a comma? \nOne has claws at the end of its paws. \nThe other is a pause at the end of a clause.", "Parallel lines have so much in common. \nIt’s a shame they’ll never meet.", "There’s a fine line between a numerator and a denominator. Only a fraction of you will get this.", "ard that Oxygen and Magnesium were dating and I was like “OMg”"]
    p = input("type joke for a joke, exit to leave: ")
    finished = []
    while p.lower() != "exit" and p.lower() != "no":
        if len(finished) == len(list):
            print("Sorry! I am out of jokes :(")
            break
        get = randint(0, len(list)-1)
        while finished.count(get) > 0:
            get = randint(0, len(list)-1)
        finished.insert(0, get)
        print("\n" + list[get])
        p = input("Again?: ")
    print("Thanks for coming! Have a great day!\n")

print ("Welcome to the Arcade! \nGAMES: See all available games! \nCOMMANDS: See all commands! \nGOOD LUCK! Note: You lose when your money reaches 0 or when you type FINISH outside of a game\n")
player = ""
while player.lower() != "done" and money > 0:
    player = input("[Lobby] What is your choice: ")
    if player.lower() == "rich":
        money += 10000000
    if player.lower() == "rps":
        rps()
    elif player.lower() == "hangman":
        hangman()
    elif player.lower() == "lot":
        lottery()
    elif player.lower() == "jokes":
        jokes()
    elif player.lower() == "commands":
        print("Type: EXIT to leave a game;\nEXIT to leave the program\nMONEY to check amount of money\nGAMES to see all games\n\n*CHEAT*\nRICH to get 1 million dollars\n")
    elif player.lower() == "money":
        print("Money: " + str(money))
    elif player.lower() == "exit":
        break
    elif player.lower() == "games":
        print()
        print("rps: rock paper scissors\nhangman: Hangman without clues\nlot: lottery (NO gambling :) )\njokes: teacher jokes\n")
    else:
        print("Try Again")
        continue
print("You ended with: " + str(money) + " dollars!")
print("Thanks for playing! Come again")