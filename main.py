from kata-range-package import Range
import os

def main():
    print("This is the kata range application")
    entered_range = input("Please enter your range: ")

    try: 
        firstRange = Range(entered_range)
        while (True):
            os.system('cls') if (os.name == "nt") else os.system('clear')
            
