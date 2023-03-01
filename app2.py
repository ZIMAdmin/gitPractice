import random
import pandas as pd
from datetime import date

today = date.today()
playAgainOption = "Yes"

while playAgainOption == "Yes":
    print("Lets play RPS.  Please choose (R)ock, (P)aper, or (S)cissors \n")
    input1 = input()

    computerChoices = ('Rock', 'Paper', 'Scissor')
    computerAnswer = random.choice(computerChoices)

    if input1 == "R":
        wordInput = "Rock"
        if computerAnswer == "Rock":
            print ("\n Player chose:" + wordInput +"\nComputer Chose:" + computerAnswer + "\n \n ITS A TIE!")
        if computerAnswer == "Paper":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n COMPUTER WINS!")
        if computerAnswer == "Scissors":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n YOU WIN!")
    elif input1 == "S":
        wordInput = "Scissors"
        if computerAnswer == "Rock":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n COMPUTER WINS!")
        if computerAnswer == "Paper":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n YOU WIN!")
        if computerAnswer == "Scissors":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n ITS A TIE!")
    elif input1 == "P":
        wordInput = "Paper"
        if computerAnswer == "Rock":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n YOU WIN!")
        if computerAnswer == "Paper":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n ITS A TIE!")
        if computerAnswer == "Scissors":
            print ("\n Player chose:" + wordInput +"\n Computer Chose:" + computerAnswer + "\n \n COMPUTER WINS!")
    else:
        print("please choose either R, P, or S for (R)ock, (P)aper, or (S)cissors")
    

    while playAgainOption2 != "No" and playAgainOption2 != "Yes":
        print("\n Would you like to play again? (Y)es or (N)o")
        playAgainOption2 = input()
        if playAgainOption2 == "Y":
            playAgainOption2 = "Yes"
        elif playAgainOption2 == "N":
            playAgainOption2 = "No"
        else:
            print("Please either choose Y or N, for (Y)es or (N)o")
            


