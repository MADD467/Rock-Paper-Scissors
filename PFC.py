import random

choix = ("Rock", "Paper", "Scissors")
computer = random.choice(choix)


for i in range(3):
    
    player = input("Rock, Paper, Scissors :")
    print("Robot a choisit: ", computer)
    
    if player == "Rock" and computer == "Rock":
        print("EGALITE")
    elif player == "Rock" and computer == "Paper":
        print("PERDU")
    elif player == "Rock" and computer == "Scissors":
        print("GAGNE")
        
    if player == "Paper" and computer == "Rock":
        print("GAGNER")
    elif player == "Paper" and computer == "Paper":
        print("EGALITE")
    elif player == "Paper" and computer == "Scissors":
        print("PERDU")
        
    if player == "Scissors" and computer == "Rock":
        print("PERDU")
    elif player == "Scissors" and computer == "Paper":
        print("GAGNER")
    elif player == "Scissors" and computer == "Scissors":
        print("EGALITE")

        