import random
import mylogos



mylogos.whylogo()
mylogos.heading()
start = int((input("SELECT ANY ONE : ")))

if start == 1:
    print("Lets Start the Game") 
    user_name = str(input("Please Enter Your Name: "))
    lol = input(f"Welcome {user_name}. Please Press Enter To Start The Game \n")
    score = 0
    com_score = 0
    while score < 5 and com_score < 5:
        qus = print("1.Rock\n2.Paper\n3.Sesior")
        ans  = int(input("Chose Any one from 1 to 3: "))
        com = random.randint(1,3)

        if ans == 1 and com == 1:   
            print("This is a Draw")
            print(f"Com : {com_score} vs {user_name} : {score}\n")
        elif ans == 1 and com == 2: 
            print("Computer Chose Paper won, You lose")
            com_score = com_score + 1
            print(f"Com : {com_score} vs {user_name} : {score}\n")
        elif ans == 1 and com == 3:
            print("Rock won, You Have Gained One point")
            score = score + 1
            print(f"Com : {com_score} vs {user_name} : {score}\n")
   
        elif ans == 2 and com == 1:
            print("Paper Won, You Have Gained One point")
            score = score + 1
            print(f"Com : {com_score} vs {user_name} : {score}\n")
        elif ans == 2 and com == 2:
            print("This is a Draw")
            print(f"Com : {com_score} vs {user_name} : {score}\n")
        elif ans == 2 and com == 3: 
            print("Computer Chose Sesior won, You lose")
            com_score = com_score + 1
            print(f"Com : {com_score} vs {user_name} : {score}\n")
        
        elif ans == 3 and com == 1:
            print("Computer Chose Rock, You lose")
            com_score = com_score + 1
            print(f"Com : {com_score} vs {user_name} : {score}\n")
        elif ans == 3 and com == 2:
            print("Sesior won, You Have Gained One point")
            score = score + 1
            print(f"Com : {com_score} vs {user_name} : {score}\n")
        elif ans == 3 and com == 3:
            print("This is a Draw")
            print(f"Com : {com_score} vs {user_name} : {score}\n")
        else:
            print("Plese Select one from 1 to 3")

    if score == 5:
        print("\n WINNER WINNER CHICKEN DINNER")
    elif com_score == 5:
        print("\nOPPS, Better Luck Next Time.")
    else:
        print("\nErro Occurred")
        
        
elif start == 2:
    mylogos.rule()
elif start == 3:
    mylogos.credit()
elif start == 4:
    mylogos.rules()
     

