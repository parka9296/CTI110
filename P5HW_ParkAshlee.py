#Ashlee Park
#7/12/25
#P5HW
#program for a game


print("🎪🎡WELCOME TO THE FAIR!🎡🎪\n")

print("Win all 3 games 🏆🏆🏆 and win a prize!!🎁\n")

print("🤹LET'S PLAY!🤹\n")

tokens=10

def play():
    global tokens
    print("🟡Tokens:", tokens)
    print("Pay token:")
    tokens-=1
    print("Tokens Remaining:", tokens, "\n")
    if tokens<0:
        exit_if=True
        print("Sorry, You're of of tokens. Better luck next time")
        return
    cups()  
    
def play1():
    global tokens
    print("🟡Tokens:", tokens)
    print("Pay token:")
    tokens-=1
    print("Tokens Remaining:", tokens, "\n")
    if tokens<0:
        exit_if=True
        print("Sorry, You're of of tokens. Better luck next time")
        return
    RPS()

def play2():
    global tokens
    print("🟡Tokens:", tokens)
    print("Pay token:")
    tokens-=1
    print("Tokens Remaining:", tokens, "\n")
    if tokens<0:
        exit_if=True
        print("Sorry, You're of of tokens. Better luck next time")
        return
    high_low()
        
def cups():
    print("🌀GAME #1: 🔵 🔴 WHICH CUP IS THE BALL UNDER? 🔴🔵\n")
    
    player_choice=input("Type Left, Middle, or Right to choose a cup:").lower().strip()
    
    import random
    options=["Left", "Right", "Middle"]
    ball=random.choice(options)
    
    print("CUP REVEAL:", ball, "\n")
    cup_reveal=ball.lower().strip()
    
    if player_choice==cup_reveal:
        print("YOU WIN! 🏆\n")
        play1()
    else:
        print("Try again ❌\n")
        play()
        
        
        
def RPS():
    print("🌀GAME #2: 🪨ROCK, 📄PAPER, ✂️SCISSORS\n")
    
    player=input("Player: ").lower().strip()
    
    import random
    options=["rock", "paper", "scissors"]
    
    choice=random.choice(options)
    
    print("Computer:", choice, end=" ")
    computer=choice
    print("\n")
    
    if player==computer:
       print("*Tie*\n")
       play1()
    elif (player=="rock" and computer=="scissors") or (player=="paper" and computer=="rock") or (player=="scissors" and computer=="paper"):
       print("*WIN*🏆🏆\n")
       play2()
    else:
        print("Try again❌\n")
        play1()
        
        
        
def high_low():
    print("🌀GAME #3: HIGHER⬆️ or LOWER⬇️\n")
    
    print("Choose a card ♣️1 through 10:♠️", end=" ")
    player=int(input())
    
    player2=input("Is your card higer or lower? ").lower().strip()
    
    import random
    card=random.randint(1,10)
    
    print("Computer:", card, "\n")
    computer=card
    
    if player>computer and player2=="higher" or player<computer and player2=="lower":
        print("YOU WIN!🏆🏆🏆\n")
        print("🎉CONGRATULATIONS!!🎉 YOU'VE WON ALL 3 GAMES!!🎉\n")
        print("1. 🎁")
        print("2. 🎁")
        print("3. 🎁")
        print("\n")

        player_pick=input("type 1, 2, or 3 to Choose Your Prize!:")
        prizes=["1", "2", "3"]
        player_pick==prizes
        print("\n")

        if player_pick=="1":
            print ("YOU'VE WON: 🧸 *A GIANT TEDDY BEAR* 🧸\n")
        elif player_pick=="2":
            print ("YOU'VE WON: 🏀 *A BASKETBALL* 🏀\n")
        else:
            print ("YOU'VE WON: 🎟️ *A FREE ADMISSION TICKET* 🎟\n️")
           
        print("👋 THANKS  FOR PLAYING!! 👋")

    else:
        print("Try again❌\n")
        play2()
        
        
if __name__ == "__main__":
    play()
           

