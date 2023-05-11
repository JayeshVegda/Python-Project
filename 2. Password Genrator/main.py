import random
import time
import os

class PasswordGenerator:
    
    def __init__(self):
        self.password = ""
        self.n = ""
        self.default_n = 4
        self.default_word = 3
        self.default_symbol = ['-', '$', '&']
        self.symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '/', '?', '|', '\\', '`', '~',]
        self.word_list = ['a', 'an', 'the', 'and', 'but', 'or', 'if', 'then', 'while', 'for', 'to', 'in', 'of', 'with', 'on', 'at', 'by', 'from', 'up', 'about', 'into', 'over', 'after', 'beneath', 'under', 'above', 'near', 'before', 'beside', 'between', 'behind', 'among', 'around', 'through', 'during', 'until', 'against', 'across', 'outside', 'inside', 'onto', 'into', 'toward', 'upon', 'off', 'over', 'out', 'down', 'up', 'on', 'off', 'out', 'down', 'up', 'on', 'off', 'out', 'down', 'very', 'so', 'such', 'just', 'only', 'now', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'what', 'who', 'whom', 'whose', 'which', 'that', 'this', 'these', 'those', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'mine', 'yours', 'his', 'hers', 'its', 'ours', 'theirs', 'me', 'you', 'him', 'her', 'it', 'us', 'them', 'that', 'which', 'who', 'whom', 'whose', 'anybody', 'anyone', 'anything', 'each', 'either', 'everybody', 'everyone', 'everything', 'neither', 'nobody', 'no one', 'nothing', 'one', 'somebody', 'someone', 'something', 'both', 'few', 'many', 'several', 'all', 'any', 'more', 'most', 'some', 'none', 'such', 'every', 'no', 'least', 'own' ] 
        self.custom_word_list = []
        self.Alphabates_list = ['a', ]
        
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
            self.complex()
        elif gen_choice == 3:
            self.memoriable()
        elif gen_choice == 4:
            self.start()
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

    def complex(self):
        self.my_logo()
        complex_password = ""
        word_length = input(f"\nEnter the length of Password (Default=8 Max=32) : ")
        ask_number = input("Do you want to use numbers (y/n): ")
        ask_symbol = input("Do you want to use special Symbol (y/n): ")
        ask_alpha = input("Do you want to use Alphabates (y/n): ")
        
        
        
        
    
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
            print(memoriable_password)
            self.continue_memoriable()
            
        elif ask_word != "y" and ask_symbol == "y":
            #print("Usual list + symbols")
            
            word_list = self.word_list
            symbol_list =  self.symbol_list
            
            for i in range(word_length):
                word = random.choice(word_list)
                symbol = random.choice(symbol_list)
                memoriable_password += word + symbol
            print(memoriable_password)
            self.continue_memoriable()
            
        elif ask_word != "y" and ask_symbol != "y":
            
            word_list = self.word_list 
            
            for i in range(word_length):
                word = random.choice(word_list)
                memoriable_password += word
            print(memoriable_password)
            self.continue_memoriable()
            
        else:
            print("error occure")
                


    def setting(self):
        pass
    
    def credit(self):
        pass
    
    def exito(self):
        pass    
    
    def start(self):
        os.system("cls")
        self.logo()
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
            self.exit()
        else:
            print("Invalid Choice")
            time.sleep(1)
            self.start()
        
        
        

if __name__ == "__main__":
    password = PasswordGenerator()
    password.start()