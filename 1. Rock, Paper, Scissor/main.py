import random
import time
import os 
import ctypes
import string

class game():
    
    def __init__(self):
        self.user = ""
        self.user_score = 0
        self.com_score = 0
        self.round = 5 
        
    def slowType(self, text: str, speed: float, newLine=True):
       for i in text:  # Loop over the message
        # Print the one charecter, flush is used to force python to print the char
        print(i, end="", flush=True)
        time.sleep(speed)  # Sleep a little before the next one
        if newLine:  # Check if the newLine argument is set to True
            print()  # Print a final newline to make it act more like a normal print statement
    def whylogo(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        if os.name == "nt":  # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Rock, Paper, Scissor - Mafe by Jayesh Vegda")  # Change the
        else:  # Or if it is unix
            print(f'\33]0;Rock, Paper, Scissor - Made by Jayesh Vegda\a',
                  end='', flush=True)  # Update title of command prompt
        print("""
        ██████╗░██████╗░░██████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
        ██╔══██╗██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
        ██████╔╝██████╔╝╚█████╗░  ██║░░██╗░███████║██╔████╔██║█████╗░░
        ██╔══██╗██╔═══╝░░╚═══██╗  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
        ██║░░██║██║░░░░░██████╔╝  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
        ╚═╝░░╚═╝╚═╝░░░░░╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")
    
    def heading(self):
        self.whylogo()
        time.sleep(1)
        print("\n")
        print("Select Any One Option from below")
        print("1. Start The Game")
        print("2. Read Rules of The Game")
        print("3. See the Credits")
        print("4. Modify Settings")
        print("5. Exit The Game")

    def rule(self):
        os.system("cls")
        self.whylogo()
        print("""- Rock Paper Scissors is Easiest Game. \n- Rock beats scissors, scissors beat paper, and paper beats rock. \n- Whoever scored 5 points first would win in the game. \n- Enjoy The Game! Good Luck  \n""")
        i = input("Please Enter to Return to Main Menu: ")
        self.start()
        
    def credit(self):
        os.system("cls")
        self.whylogo()
        print("""- Created By: Jayesh Vegda \n- Github: https://github.com/Jayesh.Vegda \n- Email: Jayeshvegda@gmail.com \n- Twitter: https://twitter.com/Jayesh.Vegda \n- Instagram: https://www.instagram.com/Zayu.Vegda \n""")
        i = input("Please Enter to Return to Main Menu: ")
        self.start()
    
    def settings(self):
        os.system("cls")
        self.whylogo()
        time.sleep(1)
        print("\n")
        print("Select Any One Option from below")
        print("1. Set User Name")
        print("2. Set a Round of Games")
        print("3. Return Main Menu")
        sett = int(input("Enter Valid Number : "))
        
        if sett in range(0,4):
            if sett == 1:
                u_sett = str(input("\n Enter Your User Name : "))
                self.user = u_sett
                self.settings()
            elif sett == 2:
                r_sett = int(input("How Many Rounds You Want To Play (Default round = 5) : "))
                if r_sett < 10:
                    self.round = r_sett
                    i = input("Please Enter to Return to Main Menu: ")
                    self.settings()
                else:
                    print("You can not set more then 10 rounds try again ")
                    i = input("Please Enter to Return to Main Menu: ")
                    self.settings()
            elif sett == 3 or sett == "main" or sett == "3":
                self.start()
            else:
                print("Enter a Valid Number")
        else:
            input("Specified input wasn't a number.\nPress enter to return to Main Menu")
            self.settings()
      
    
    def ex(self):
        self.whylogo()
        time.sleep(1)  # Wait a few seconds
        # Print who developed the code5
        print("")
        print("")
        self.slowType("Good Bye ! See You Soon !", .02, newLine=False)
        time.sleep(1)  # Wait a little more
        print("")
        self.slowType("Made by Jayesh Vegda",.02, newLine=False)
        time.sleep(2)  # Wait a little more
        # Print the first question
        os.sys("cls")
    
    def main(self):
        
      
            
        os.system("cls")
        self.whylogo()
        print("")
        
        user_score = 0
        com_score = 0
       
        
        if self.user == "":
            self.user = str(input("ENTER YOUR NAME: "))
        else:
            pass
        
        
       
        
        while user_score < self.round and com_score < self.round:
            ran = random.randint(1, 3)
            os.system("cls")
            self.whylogo()
            print("")
            print(f"{self.user} : {user_score} | Comptuer : {com_score} ")
            print("")
            print("Select Any one\n 1.Rock \n 2.Paper\n 3.Scissors")
            self.Chose = int(input("Chose Any one: "))
            if self.Chose in range(0,4):
                if self.Chose == 1 and ran == 1:
                    print("Computer Selected Rock")
                    print("Its a Draw")
                    time.sleep(1)
                    
                elif self.Chose == 1 and ran == 2:
                    print("Computer Selected Paper")
                    print("You Lose !")
                    com_score = com_score + 1
                    time.sleep(1)
                    
                elif self.Chose == 1 and ran == 3:
                    print("Compter Selected Sessior")
                    print("Hurray ! You Gain one Point ")
                    user_score = user_score + 1
                    time.sleep(1)
                
                elif self.Chose == 2 and ran == 1: 
                    print("Computer Selected Rock")
                    print("Hurray ! You Gained one Point")
                    user_score = user_score + 1
                    time.sleep(1)
                    
                elif self.Chose == 2 and ran == 2:
                    print("Computer Selected Paper")
                    print("Its a Draw")
                    time.sleep(1)
                    
                elif self.Chose == 2 and ran == 3:
                    print("Computer Selected Sessior")
                    print("You Lose !")
                    com_score = com_score + 1
                    time.sleep(1)
                
                elif self.Chose == 3 and ran == 1:
                    print("Computer Selected Rock")
                    print("You Lose !")
                    com_score = com_score + 1
                    time.sleep(1)
                    
                elif self.Chose == 3 and ran == 2:
                    print("Computer Selected Paper")
                    print("Hurray ! You have Gained one point")
                    user_score = user_score + 1
                    time.sleep(1)
                    
                elif self.Chose == 3 and ran == 3:
                    print("Its a Draw")
                    time.sleep(1)
            else:
                print("Enter a valid number")
        
        if com_score == self.round:
            os.system("cls")
            self.whylogo()
            print("")
            print("Computer Won the Game ! ")
            input("Press enter to go back to main menu")
            self.start()
        elif user_score == self.round:
            os.system("cls")
            self.whylogo()
            print("")
            print("Computer Won the Game ! ")
            input("Press enter to go back to main menu")
            self.start()
        else:
            os.system("cls")
            self.whylogo()
            print("")
            print("Error running")
            input("Press enter to go back to main menu")
            self.start()

    
    def start(self):
        os.system("cls")
        self.heading()
        self.head_ques = int(input("Your Select Number is : "))
        if self.head_ques in (n := [1, 2, 3, 4, 5]):            
            if self.head_ques == 1:
                self.main()
            elif self.head_ques == 2:
                self.rule()
            elif self.head_ques == 3:
                self.credit()
            elif self.head_ques == 4:
                self.settings()
            elif self.head_ques == 5:
                self.ex()
            else:
                print("Select a Valid Number")        
    
if __name__ == '__main__':
    g = game()
    g.start()