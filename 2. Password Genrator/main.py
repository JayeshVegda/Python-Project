import random
import time
import os

class PasswordGenerator:
    
    range_list{
        4: (1000, 9999),
        5: (10000, 99999),
        6: (100000, 999999),
        7: (1000000, 9999999),
        8: (10000000, 99999999),
        9: (100000000, 999999999),
        10: (1000000000, 9999999999)
        11: (10000000000, 9999999999),
        12: (10000000000, 99999999999),
        13: (100000000000, 99999999999)
    }
    def __init__(self):
        self.password = ""
        
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
        
        gen_choice = input("Enter your choice: ")
        
        if gen_choice == "1":
            self.pin()
        elif gen_choice == "2":
            self.complex()
        elif gen_choice == "3":
            self.memoriable()
        else:
            print("Invalid Choice")
            time.sleep(1)
            self.generate()
    
    def pin(self):
        self.my_logo()
        print("\nSelect any one from the menu below: ")
        pin_length = int(input("Enter the length of the password (default = 4): "))
        input("Press Enter to Genrate Password...... ")
        
        
        
        if pin_length == "":
            ran = random.randint(1000, 9999)
            self.password = ran 
            print(self.password)
        elif pin_length < 3:
            print("Please enter a value greater than 3")
            time.sleep(1)
            self.pin()
        elif pin_length >= 4:
                            
            ran = random.randint(1000, 9999)
            self.password = ran 
            print(self.password)
        
        
        
        
    
    def complex(self):
        pass
    
    def memoriable(self):
        pass
    
    
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