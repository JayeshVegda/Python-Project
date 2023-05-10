import random
import time
import os 



class game():
    
    def __init__(self):
        self.user = ""
        self.user_score = 0
        self.com_score = 0
        self.round = 5 
        
    def whylogo(self):
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
        print("4. Exit The Game")

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
        
    def exio(self):
        exit()
        
    
    
    def main(self):
        os.system("cls")
        self.whylogo()
        print("")
        
        user_score = 0
        com_score = 0
        ran = random.randint(1, 3)
        
        if self.user == "":
            self.user = str(input("ENTER YOUR NAME: "))
        else:
            pass
        
        os.system("cls")
        self.whylogo()
        print("")
        print(f"Welcome {self.user}, Lets Begin the game!")
        print("")
        print("Select Any one\n 1.Rock \n 2.Paper\n 3.Scissors")
        self.Chose = int(input("Chose Any one: "))
        
        if self.Chose == 1 and ran == 1:
            print("Computer Selected Rock")
            print("Its a Draw")
        elif self.Chose == 1 and ran == 2:
            print("Computer Selected Paper")
            print("You Lose !")
            com_score = com_score + 1
        elif self.Chose == 1 and ran == 3:
            print("Compter Selected Sessior")
            print("Hurray ! You Gain one Point ")
            user_score = user_score + 1
        
        elif self.Chose == 2 and ran == 1: 
            print("Computer Selected Rock")
            print("Hurray ! You Gained one Point")
            user_score = user_score + 1
        elif self.Chose == 2 and ran == 2:
            print("Computer Selected Paper")
            print("Its a Draw")
        elif self.Chose == 2 and ran == 3:
            print("Computer Selected Sessior")
            print("You Lose !")
            com_score = com_score + 1
        
        elif self.Chose == 3 and ran == 1
    
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
                exit()
            else:
                print("Select a Valid Number")        
    
if __name__ == '__main__':
    g = game()
    g.start()