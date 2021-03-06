from Multiplications import Multiply
import os


def main():
    while True:
        #os.system('cls')
        print("------------------------------")
        print("Menu : ")
        print("Enter 1 to choose a table")
        print("Enter 2 for a random table")
        print("Enter 3 to quit")
        print("------------------------------")
        user_menu_choice = (int(input()))

        if user_menu_choice is 1:
            print("Choose a table: ")
            user_choice = (int(input()))
            multi = Multiply(user_choice)
            multi.calculate_result(user_menu_choice)
            user_answer = (int(input()))
            multi.evaluate_result(user_answer)
        elif user_menu_choice is 2:
            multi = Multiply()
            multi.calculate_result()
            user_answer = (int(input()))
            multi.evaluate_result(user_answer)
        elif user_menu_choice is 3:
            print('Program terminated')
            quit()
        else:
            print("Wrong option - should be 1, 2 or 3")


# Main
if __name__ == '__main__':
    # Runs the application
    main()
