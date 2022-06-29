from click import option
from kata-range-package import Range
import os

def main():
    print("This is the kata range application")
    entered_range = input("Please enter your range: ")

    try: 
        firstRange = Range(entered_range)
        while (True):
            os.system('cls') if (os.name == "nt") else os.system('clear')
            print("Choose the operation you want to perform")
            operationSelected = input("1. Endpoints" + "2. Get all points" + "3. Equals" + "4 Overlaps" + "5. Close program")
        
            if(operationSelected == '1'):
                value = firstRange.endpoints
                print(f"{value}")
            
            elif(operationSelected == '2'):
                value = firstRange.getAllPoints()
                print(f"{value}")
                pass

            elif(operationSelected == '3'):
                second_range = input("Please enter the second range: ")
                first_range = Range(entered_range)
                value = first_range.equals(second_range)
                print(f"{value}")
                pass
            
            elif(operationSelected == '4'):
                second_range = input("Please enter the second range: ")
                first_range = Range(entered_range)
                value = first_range.overlapsRange(second_range)
                print(f"{value}")
                pass
            elif(operationSelected == '5'):
                print("Close application")
                break
    
    except (Exception, ValueError, SyntaxError, TypeError):
        print(f"Something went wrong, please check your input")

if __name__ == "__main__":
    main()
    pass



