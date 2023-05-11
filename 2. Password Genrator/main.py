import random
import time
import os
import ctypes

class PasswordGenerator:

    def __init__(self):
        self.password = ""
        self.n = ""
        self.default_n = 4
        self.default_word = 3
        self.default_complexes = 0
        self.default_symbol = ['-', '$', '&']
        self.symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '|', '\\', '`', '~',]
        self.word_list = ['a', 'an', 'the', 'and', 'but', 'or', 'if', 'then', 'while', 'for', 'to', 'in', 'of', 'with', 'on', 'at', 'by', 'from', 'up', 'about', 'into', 'over', 'after', 'beneath', 'under', 'above', 'near', 'before', 'beside', 'between', 'behind', 'among', 'around', 'through', 'during', 'until', 'against', 'across', 'outside', 'inside', 'onto', 'into', 'toward', 'upon', 'off', 'over', 'out', 'down', 'up', 'on', 'off', 'out', 'down', 'up', 'on', 'off', 'out', 'down', 'very', 'so', 'such', 'just', 'only', 'now', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'what', 'who', 'whom', 'whose', 'which', 'that', 'this', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs', 'me', 'you', 'him', 'her', 'it', 'us', 'them', 'that', 'which', 'who', 'whom', 'whose', 'anybody', 'anyone', 'anything', 'each', 'either', 'everybody', 'everyone', 'everything', 'neither', 'nobody', 'no one', 'nothing', 'one', 'somebody', 'someone', 'something', 'both', 'few', 'many', 'several', 'all', 'any', 'more', 'most', 'some', 'none', 'such', 'every', 'no', 'least', 'own' ] 
        self.custom_word_list = []
        self.number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.Alphabates_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
    def random_with_N_digits(self, n):
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return random.randint(range_start, range_end)
    

    def logo(self):  
        print(""" 
                
        ░██████╗░███████╗███╗░░██╗  ██████╗░░█████╗░░██████╗░██████╗
        ██╔════╝░██╔════╝████╗░██║  ██╔══██╗██╔══██╗██╔════╝██╔════╝
        ██║░░██╗░█████╗░░██╔██╗██║  ██████╔╝███████║╚█████╗░╚█████╗░
        ██║░░╚██╗██╔══╝░░██║╚████║  ██╔═══╝░██╔══██║░╚═══██╗░╚═══██╗
        ╚██████╔╝███████╗██║░╚███║  ██║░░░░░██║░░██║██████╔╝██████╔╝
        ░╚═════╝░╚══════╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝░░╚═╝╚═════╝░╚═════╝░""")
    
    def my_logo(self):
        os.system("cls")
        self.logo()
        time.sleep(1)
        
    def generate(self):
        self.my_logo()
        print("\nSelect any one from the menu below: ")
        print("1. Pin Password")
        print("2. Complex Password")
        print("3. Memoriable Password")
        print("4. Return to Main Menu")
        
        gen_choice = int(input("Enter your choice: "))
        
        if gen_choice == 1:
            self.pin()
        elif gen_choice == 2:
            self.complexes()
        elif gen_choice == 3:
            self.memoriable()
        elif gen_choice == 4:
            self.exito()
        else:
            print("Invalid Choice")
            time.sleep(1)
            self.generate()
    
    def pin(self):
        self.my_logo()
        pin_length = input(f"\nEnter the length of the password (default = {self.default_n}): ")
        if pin_length.strip() == "":
            pin_length = self.default_n
        else:
            pin_length = int(pin_length)

        try:
            if pin_length < 4:
                print("Please enter a value greater than or equal to 4")
                time.sleep(2)
                self.pin()
            elif pin_length > 32:
                print("Please enter a value less than or equal to 32")
                time.sleep(2)
                self.pin()
            else:
                password = self.random_with_N_digits(pin_length)
                print(f"Your Genrated Pin is {password}")
                self.password = password
                bye = input("Enter to continue or write anything to return to main menu: ")
                if bye.strip() == "":
                    self.pin()
                else:
                    print("Returning to main menu")
                    time.sleep(1)  
                    self.start() 
        except:
            print("Error Occure")

    def complexes(self):
        self.my_logo()
        complex_password = ""
        if self.default_complexes == 0:
            word_length = int(input(f"\nEnter the length of Password (Default=8 Max=32) : "))
        else:
            word_length = self.default_complexes
            print("Your Default Length is : ", word_length)
            
        input("Please Enter to Genrate your Password....")
        
        for i in range(word_length):
            word = random.choice(self.Alphabates_list)
            symbol = random.choice(self.symbol_list)
            number = random.randint(1, 10)
            complex_password += word + symbol + str(number)
            final = complex_password[0:word_length]
        
        print("\nYour Genrated Password is : ", final)
        leave = input("\nEnter to Continue or write exit to leave :")
        if leave.strip() == "":
            self.complexes()
        else:
             print("Returning to main menu")
             time.sleep(1)  
             self.start()
   
    def continue_memoriable(self):
        leave = input("\nEnter to Continue or write exit to leave :")
        if leave.strip() == "":
            self.memoriable()
        else:
            self.start()
    
    def memoriable(self):
        self.my_logo()
        memoriable_password = ""
        word_length = input(f"\nEnter the minimun word list (default = {self.default_word}) : ")
        if self.custom_word_list == []:
            ask_word = input("Do you want to add use custom words list (y/n): ")
            if ask_word == "y":
                while True:
                    word = input("Enter the word (Leave blank to exit): ")
                    if word.strip() == "":
                        break
                    else:
                        self.custom_word_list.append(word)
                print(self.custom_word_list)
            else:
                print("Continue.... \n")
        else:
            ask_word = "y"
            
        ask_symbol = input("Do you want to add special Symbol (y/n): ")
        if ask_symbol == "y":
            print("yes")
        else:
            print("Continue.... \n")
            
        if word_length.strip() == "":
            word_length = self.default_word
        else: 
            word_length = int(word_length)
            
        
        input("Please Enter to Genrate your Password....")
        
        if ask_word == "y" and ask_symbol == "y":
            #print("custom list + add symbols")
            
            word_list = self.custom_word_list
            symbol_list = self.symbol_list
            
            for i in range(word_length):
                word = random.choice(word_list)
                symbol = random.choice(symbol_list)
                memoriable_password += word + symbol
            print("Your Genrated Password is \n ", memoriable_password)
            self.continue_memoriable()
            
        elif ask_word == "y" and ask_symbol != "y":
            #print("Custom list + no symbols")
            word_list = self.custom_word_list
            
            for i in range(word_length):
                word = random.choice(word_list)
                memoriable_password += word
            print("Your Genrated Password is \n ", memoriable_password)
            self.continue_memoriable()
            
        elif ask_word != "y" and ask_symbol == "y":
            #print("Usual list + symbols")
            
            word_list = self.word_list
            symbol_list =  self.symbol_list
            
            for i in range(word_length):
                word = random.choice(word_list)
                symbol = random.choice(symbol_list)
                memoriable_password += word + symbol
            print("Your Genrated Password is \n ", memoriable_password)
            self.continue_memoriable()
            
        elif ask_word != "y" and ask_symbol != "y":
            
            word_list = self.word_list 
            
            for i in range(word_length):
                word = random.choice(word_list)
                memoriable_password += word
            print("Your Genrated Password is \n ", memoriable_password)
            self.continue_memoriable()
            
        else:
            print("error occure")
                


    def setting(self):
        self.my_logo()
        print("\nSelect any one from the menu below: ")
        print("1. Change Default Length of Password")
        print("2. Add Custom Words List")
        print("3. Return to Main Menu")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            selected_length = int(input("Enter the length of password : "))            
            self.default_complexes = selected_length
            print(f"Your Default Length is {selected_length}, {self.default_complexes}")
            input("Plese Press Enter to Return Main Menu")
            time.sleep(1)
            self.setting()
        elif choice == 2:
            while True:
                word = input("Enter the word (Leave blank to exit): ")
                if word.strip() == "":
                    break
                else:
                    self.custom_word_list.append(word)
            print(self.custom_word_list)
            input("Plese Press Enter to Return Main Menu")
            time.sleep(1)
            self.setting()
        elif choice == 3:
            self.start()
        else:
            print("Invalid Choice")
            time.sleep(1)
            self.setting()
        
    
    def credit(self):
        os.system("cls")
        self.my_logo()
        print("""\n- Created By: Jayesh Vegda \n- Github: https://github.com/Jayesh.Vegda \n- Email: Jayeshvegda@gmail.com \n- Twitter: https://twitter.com/Jayesh.Vegda \n- Instagram: https://www.instagram.com/Zayu.Vegda \n""")
        input("\nPlease Enter to Return to Main Menu: ")
        time.sleep(1)
        self.start()
            
    def exito(self):
        os.system("cls")
        self.my_logo()
        print("\n Good Bye ! Have a Good Day ahead")
        time.sleep(2)
        exit()
    
    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        if os.name == "nt":  # If the system is windows
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Password Genrator - Mafe by Jayesh Vegda")  # Change the
        else:  # Or if it is unix
            print(f'\33]0;Password Genrator - Made by Jayesh Vegda\a',
                  end='', flush=True)  # Update title of command prompt
        os.system("cls")
        self.my_logo()
        time.sleep(1)
        print("\nSelect Any one from the menu below: ")
        print("1. Generate Password")
        print("2. Modify Settings")
        print("3. Credit")
        print("4. Exit Program")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            self.generate()
        elif choice == "2":
            self.setting()
        elif choice == "3":
            self.credit()
        elif choice == "4":
            self.exito()
        else:
            print("Invalid Choice")
            time.sleep(1)
            self.start()
        
        
        

if __name__ == "__main__":
    password = PasswordGenerator()
    password.start()