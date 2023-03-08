import random
import time
from datetime import date

today = date.today()
playAgainOption = "Yes"

while playAgainOption == "Yes":
    print("\nLets play RPS.  Please choose (R)ock, (P)aper, or (S)cissors \n")
    input1 = input()
    time.sleep(3)
    computerChoices = ('Rock', 'Paper', 'Scissor')
    computerAnswer = random.choice(computerChoices)
    if input1 == "R" or input1 == "r":
        wordInput = "Rock"
        if computerAnswer == "Rock":
            print ("\n Player chose:" + wordInput +"\nComputer Chose:" + computerAnswer + "\n \n ITS A TIE!")
        if computerAnswer == "Paper":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n COMPUTER WINS!")
        if computerAnswer == "Scissors":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n YOU WIN!")
    elif input1 == "S" or input1 == "s":
        wordInput = "Scissors"
        if computerAnswer == "Rock":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n COMPUTER WINS!")
        if computerAnswer == "Paper":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n YOU WIN!")
        if computerAnswer == "Scissors":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n ITS A TIE!")
    elif input1 == "P" or input1 == "p":
        wordInput = "Paper"
        if computerAnswer == "Rock":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n YOU WIN!")
        if computerAnswer == "Paper":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n ITS A TIE!")
        if computerAnswer == "Scissors":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n COMPUTER WINS!")
    else:
        print("please choose either R, P, or S for (R)ock, (P)aper, or (S)cissors \n")
        continue

    time.sleep(3)
    print("\n Would you like to play again? (Y)es or (N)o")
    playAgainOption = input()
    if playAgainOption == "Y" or playAgainOption=="y":
        playAgainOption = "Yes"
    elif playAgainOption == "N" or playAgainOption=="n":
        playAgainOption = "No"
    else:
        print("Please either choose Y or N, for (Y)es or (N)o")
        continue
    


