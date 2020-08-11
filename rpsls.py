# ## Importing functions and/or modules.
import sys
import time
from os import system
from random import randint
from getpass import getpass


def display_main_menu():
    """

    Prints the main menu line by line.

    """
    print("Welcome to Rock, Paper, Scissor, Lizard, Spock!\n",
          "1: New Single Player Game",
          "2: New Two Player Game",
          "3: Bonus Feature",
          "4: User Guide",
          "Q: Quit\n", sep="\n", end="\n")
    return ""


def display_single_menu():
    """

    Prints the single player menu line by line.

    """
    print("Welcome to single player mode!\n",
          "1: Rock",
          "2: Paper",
          "3: Scissors",
          "4: Lizard",
          "5: Spock",
          "Q: Quit\n", sep="\n", end="\n")
    return ""


def display_multi_menu():
    """

    Prints the two player menu line by line.

    """
    print("Welcome to two player mode!\n",
          "1: Rock",
          "2: Paper",
          "3: Scissors",
          "4: Lizard",
          "5: Spock",
          "Q: Quit\n", sep="\n", end="\n")
    return ""


def display_bonus_menu():
    """

    Prints the bonus menu line by line.

    """
    print("Welcome to the Big Bang Theory trivia quiz!\n",
          "1: True",
          "2: False",
          "Q: Quit\n", sep="\n", end="\n")
    return ""


def clear_screen():
    """
    Clear terminal screen.
    Checks OS to send correct command.
    """
    if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
        _ = system('clear')
    else:
        _ = system('cls')


def wait_for_keypress():
    """

    Waits for any key to be pressed.
    Checks OS to send correct command.

    """
    if sys.platform == "linux" or sys.platform == "linux2" or sys.platform == "darwin":
        _ = system("read -s -n 1 -p \"Press any to continue....\"")
    else:
        _ = system("pause")
        print("\nPress any to continue....")


def hand_sign_selector(hand_sign):
    """

    Prints the hand sign menu line by line.

    """
    if hand_sign == "1":
        return "Rock"
    elif hand_sign == "2":
        return "Paper"
    elif hand_sign == "3":
        return "Scissors"
    elif hand_sign == "4":
        return "Lizard"
    elif hand_sign == "5":
        return "Spock"
    else:
        return hand_sign


def roulette():
    """
    Returns random string of "Rock", "Paper", "Scissor", "Lizard" or "Spock"

    """
    spin = {
        1: "Rock",
        2: "Paper",
        3: "Scissors",
        4: "Lizard",
        5: "Spock"
    }

    result = randint(1, 5)

    return spin[result]


# Displaying the main menu at the top of the screen, and entering a loop to keep menus on top.
clear_screen()
display_main_menu()

# Checks for invalid inputs.
while True:
    # Prints the main menu and requests selection.
    clear_screen()
    display_main_menu()
    main_menu_option = input("Please make a selection from the menu: ")

    # Menu option 1, single player mode.
    if main_menu_option == "1":
        # Setting score to zero for both players.
        player1_score = 0
        player2_score = 0

        # Requesting user to enter name, and assigning the computer a name.
        clear_screen()
        player1_name = input("Please enter the name of player 1: ")
        clear_screen()
        player2_name = "Sheldon"
        clear_screen()

        # Checks for invalid inputs.
        while True:
            # Updating the score.
            display_single_menu()
            print("The score is:")
            print(player1_score, "to", player1_name)
            print(player2_score, "to", player2_name)
            print("")

            # Requests player to select hand sign, randomly picks one for the computer.
            player1_choice = hand_sign_selector(
                getpass("{}, please select a hand sign using the menu options: ".format(player1_name)))
            player2_choice = roulette()
            print("")

            # if player 1 wins, returns result.
            if player1_choice == "Rock" and player2_choice == "Scissors":
                print("Rock crushes Scissors!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Rock" and player2_choice == "Lizard":
                print("Rock crushes Lizard!", player1_name, "wins!")
                player1_score += 1

            elif player1_choice == "Paper" and player2_choice == "Rock":
                print("Paper covers Rock!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Paper" and player2_choice == "Spock":
                print("Paper disproves Spock!", player1_name, "wins!")
                player1_score += 1

            elif player1_choice == "Scissors" and player2_choice == "Paper":
                print("Scissors cuts Paper!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Scissors" and player2_choice == "Lizard":
                print("Scissors decapitates Lizard!", player1_name, "wins!")
                player1_score += 1

            elif player1_choice == "Lizard" and player2_choice == "Paper":
                print("Lizard eats Paper!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Lizard" and player2_choice == "Spock":
                print("Lizard poisons Spock!", player1_name, "wins!")
                player1_score += 1

            elif player1_choice == "Spock" and player2_choice == "Rock":
                print("Spock vapourises Rock!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Spock" and player2_choice == "Scissors":
                print("Spock smashes Scissors!", player1_name, "wins!")
                player1_score += 1

            # if player 2 wins, returns result.
            elif player2_choice == "Rock" and player1_choice == "Scissors":
                print("Rock crushes Scissors!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Rock" and player1_choice == "Lizard":
                print("Rock crushes Lizard!", player2_name, "wins!")
                player2_score += 1

            elif player2_choice == "Paper" and player1_choice == "Rock":
                print("Paper covers Rock!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Paper" and player1_choice == "Spock":
                print("Paper disproves Spock!", player2_name, "wins!")
                player2_score += 1

            elif player2_choice == "Scissors" and player1_choice == "Paper":
                print("Scissors cuts Paper!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Scissors" and player1_choice == "Lizard":
                print("Scissors decapitates Lizard!", player2_name, "wins!")
                player2_score += 1

            elif player2_choice == "Lizard" and player1_choice == "Paper":
                print("Lizard eats Paper!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Lizard" and player1_choice == "Spock":
                print("Lizard poisons Spock!", player2_name, "wins!")
                player2_score += 1

            elif player2_choice == "Spock" and player1_choice == "Rock":
                print("Spock vapourises Rock!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Spock" and player1_choice == "Scissors":
                print("Spock smashes Scissors!", player2_name, "wins!")
                player2_score += 1

            # if the players have the same input
            elif player1_choice == player2_choice:
                print("You have a tie! Please try again")

            # Exits the loop, moving to the main menu
            elif player1_choice.lower() == "q" or player2_choice.lower() == "q":
                break

            # if the user inputs a value outside of the scope, print error message and continue.
            else:
                print("Invalid input! Try again")

            # Restarts the loop.
            reload = input("\nPress Enter to continue, or enter Q to quit: ")
            if reload.lower() == "q":
                break
            else:
                clear_screen()

    # Menu option 2, two player mode
    elif main_menu_option == "2":
        # Setting score to zero for both players.
        player1_score = 0
        player2_score = 0

        # Requesting both players to enter names.
        clear_screen()
        player1_name = input("Please enter the name of player 1: ")
        clear_screen()
        player2_name = input("Please enter the name of player 2: ")
        clear_screen()

        # Checks for invalid inputs.
        while True:
            # Updating the score.
            display_multi_menu()
            print("The score is:")
            print(player1_score, "to", player1_name)
            print(player2_score, "to", player2_name)
            print("")

            # Requesting players to select hand signs.
            player1_choice = hand_sign_selector(
                getpass("{}, please select a hand sign using the menu options: ".format(player1_name)))
            player2_choice = hand_sign_selector(
                getpass("{}, please select a hand sign using the menu options: ".format(player2_name)))
            print("")

            # if the user inputs a value outside of the scope, user is requested to try again.
            if player1_choice == "Invalid" or player2_choice == "Invalid":
                print("Invalid input! Please try again")

            # if player 1 wins, returns result.
            elif player1_choice == "Rock" and player2_choice == "Scissors":
                print("Rock crushes Scissors!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Rock" and player2_choice == "Lizard":
                print("Rock crushes Lizard!", player1_name, "wins!")
                player1_score += 1

            elif player1_choice == "Paper" and player2_choice == "Rock":
                print("Paper covers Rock!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Paper" and player2_choice == "Spock":
                print("Paper disproves Spock!", player1_name, "wins!")
                player1_score += 1

            elif player1_choice == "Scissors" and player2_choice == "Paper":
                print("Scissors cuts Paper!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Scissors" and player2_choice == "Lizard":
                print("Scissors decapitates Lizard!", player1_name, "wins!")
                player1_score += 1

            elif player1_choice == "Lizard" and player2_choice == "Paper":
                print("Lizard eats Paper!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Lizard" and player2_choice == "Spock":
                print("Lizard poisons Spock!", player1_name, "wins!")
                player1_score += 1

            elif player1_choice == "Spock" and player2_choice == "Rock":
                print("Spock vapourises Rock!", player1_name, "wins!")
                player1_score += 1
            elif player1_choice == "Spock" and player2_choice == "Scissors":
                print("Spock smashes Scissors!", player1_name, "wins!")
                player1_score += 1

            # if player 2 wins, returns result.
            elif player2_choice == "Rock" and player1_choice == "Scissors":
                print("Rock crushes Scissors!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Rock" and player1_choice == "Lizard":
                print("Rock crushes Lizard!", player2_name, "wins!")
                player2_score += 1

            elif player2_choice == "Paper" and player1_choice == "Rock":
                print("Paper covers Rock!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Paper" and player1_choice == "Spock":
                print("Paper disproves Spock!", player2_name, "wins!")
                player2_score += 1

            elif player2_choice == "Scissors" and player1_choice == "Paper":
                print("Scissors cuts Paper!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Scissors" and player1_choice == "Lizard":
                print("Scissors decapitates Lizard!", player2_name, "wins!")
                player2_score += 1

            elif player2_choice == "Lizard" and player1_choice == "Paper":
                print("Lizard eats Paper!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Lizard" and player1_choice == "Spock":
                print("Lizard poisons Spock!", player2_name, "wins!")
                player2_score += 1

            elif player2_choice == "Spock" and player1_choice == "Rock":
                print("Spock vapourises Rock!", player2_name, "wins!")
                player2_score += 1
            elif player2_choice == "Spock" and player1_choice == "Scissors":
                print("Spock smashes Scissors!", player2_name, "wins!")
                player2_score += 1

            # if the players have the same input
            elif player1_choice == player2_choice:
                print("You have a tie! Please try again")

            # Exits the loop, moving to the main menu
            elif player1_choice.lower() == "q" or player2_choice.lower() == "q":
                break

            # Prints error message, and continues.
            else:
                print("Invalid input! Try again")

            # Restarts the loop.
            reload = input("\nPress Enter to continue, or enter Q to quit: ")
            if reload.lower() == "q":
                break
            else:
                clear_screen()

    # Menu option 3, bonus feature
    elif main_menu_option == "3":
        clear_screen()
        quiz_score = 0

        # Checks for invalid inputs.
        while True:
            # Prints the main menu and updates the score.
            clear_screen()
            display_bonus_menu()
            print("The score is:", quiz_score)

            # Question 1, requesting answer and returning result.
            answer = input("\nThe two main characters Sheldon Cooper and Leonard Hofstadter "
                           "named after television producer Sheldon Leonard?: ")
            if answer == "1":
                quiz_score += 1
                clear_screen()
                display_bonus_menu()
                print("The score is:", quiz_score)
                print("\nCorrect")
                pass
            elif answer == "2":
                quiz_score -= 1
                clear_screen()
                display_bonus_menu()
                print("The score is:", quiz_score)
                print("\nIncorrect")
                pass
            elif answer.lower() == "m" or answer.lower() == "q":
                break
            else:
                print("Invalid input! Try again")
                wait_for_keypress()
                continue
            wait_for_keypress()

            # Checks for invalid inputs.
            while True:
                # Question 2, requesting answer and returning result.
                clear_screen()
                display_bonus_menu()
                print("The score is:", quiz_score)
                print("")

                answer = input("Leonard has no lenses in his glasses: ")
                if answer == "1":
                    quiz_score += 1
                    clear_screen()
                    display_bonus_menu()
                    print("The score is:", quiz_score)
                    print("\nCorrect")
                    wait_for_keypress()
                    break
                elif answer == "2":
                    quiz_score -= 1
                    clear_screen()
                    display_bonus_menu()
                    print("The score is:", quiz_score)
                    print("\nIncorrect")
                    wait_for_keypress()
                    break
                elif answer.lower() == "m" or answer.lower() == "q":
                    break
                else:
                    print("\nInvalid input! Try again")
                    wait_for_keypress()

            # Checks for invalid inputs.
            while True:
                # Question 3, requesting answer and returning result.
                clear_screen()
                display_bonus_menu()
                print("The score is:", quiz_score)
                print("")

                answer = input("Kaley Cuoco has a PhD in Neuroscience: ")
                if answer == "2":
                    quiz_score += 1
                    clear_screen()
                    display_bonus_menu()
                    print("The score is:", quiz_score)
                    print("\nCorrect! Mayim Bialik, the actress playing Amy has a PhD in Neuroscience")
                    wait_for_keypress()
                    break
                elif answer == "1":
                    quiz_score -= 1
                    clear_screen()
                    display_bonus_menu()
                    print("The score is:", quiz_score)
                    print("\nIncorrect! Mayim Bialik, the actress playing Amy has a PhD in Neuroscience")
                    wait_for_keypress()
                    break
                elif answer.lower() == "m" or answer.lower() == "q":
                    break
                else:
                    print("\nInvalid input! Try again")
                    wait_for_keypress()

            # Checks for invalid inputs.
            while True:
                # Question 4, requesting answer and returning result.
                clear_screen()
                display_bonus_menu()
                print("The score is:", quiz_score)
                print("")

                answer = input("Kevin Sussman, who plays Stuart Bloom the comic book store owner, "
                               "actually worked in a comic book store before becoming an actor: ")
                if answer == "1":
                    quiz_score += 1
                    clear_screen()
                    display_bonus_menu()
                    print("The score is:", quiz_score)
                    print("\nCorrect")
                    wait_for_keypress()
                    break
                elif answer == "2":
                    quiz_score -= 1
                    clear_screen()
                    display_bonus_menu()
                    print("The score is:", quiz_score)
                    print("\nIncorrect")
                    wait_for_keypress()
                    break
                elif answer.lower() == "m" or answer.lower() == "q":
                    break
                else:
                    print("\nInvalid input! Try again")
                    wait_for_keypress()

            # Checks for invalid inputs.
            while True:
                # Question 5, requesting answer and returning result.
                clear_screen()
                display_bonus_menu()
                print("The score is:", quiz_score)
                print("")

                answer = input("Howard (Simon Helberg) is the only one who "
                               "has seen Penny (Kaley Cuoco) naked in person: ")
                if answer == "2":
                    quiz_score += 1
                    clear_screen()
                    display_bonus_menu()
                    print("The score is:", quiz_score)
                    print("\nCorrect")
                    wait_for_keypress()
                    break
                elif answer == "1":
                    quiz_score -= 1
                    clear_screen()
                    display_bonus_menu()
                    print("The score is:", quiz_score)
                    print("\nIncorrect! He is the only one who hasn\'t")
                    wait_for_keypress()
                    break
                elif answer.lower() == "m" or answer.lower() == "q":
                    break
                else:
                    print("\nInvalid input! Try again")
                    wait_for_keypress()

            # Prints the result of the game after the last question
            clear_screen()
            display_bonus_menu()
            print("Your total score is: ", quiz_score)
            print("\n")

            # Exiting bonus game, returning to main menu.
            wait_for_keypress()
            break

    # Menu option 4, user guide
    elif main_menu_option == "4":
        # Prints instructions, waits for keypress and returns to main menu.
        clear_screen()
        print("""
Welcome to the User Guide!

All selections in this game are performed by pressing the appropriate digit og character, followed by pressing the Enter key; i.e. 1, 2, 3, 4 or Q + Enter
Entering Q + Enter anywhere in the game will take you back to the main menu, or exit the game.

1: New Single Player Game

	Please enter the name of player 1: "Enter your name."
	
	1: Rock
	2: Paper
	3: Scissors
	4: Lizard
	5: Spock
	Q: Quit
	
	"Your name", please select a hand sign using the menu options: 
	"Select from the menu."
	Press Enter to continue.
	
2: New Two Player Game

	Please enter the name of player 1: "Enter the first player name."
	Please enter the name of player 2: "Enter the second player name."
	
	1: Rock
	2: Paper
	3: Scissors
	4: Lizard
	5: Spock
	Q: Quit
	
	"First player name", please select a hand sign using the menu options: 
	"Select from the menu."
	"Second player name", please select a hand sign using the menu options: 
	"Select from the menu."
	Press Enter to continue.
    
3: Bonus Feature
	
	1: True
	2: False
	Q: Quit
	
	Select from the menu, followed by Enter.
	
4: User Guide
	
	Press Enter to go back to the main menu.
	
Q: Quit
	
	Enter Q to exit the game.
""")

        wait_for_keypress()

    # Menu option Q, quit game. Display message for 1 second.
    elif main_menu_option.lower() == "q":
        clear_screen()
        print("Thank you for playing!")
        time.sleep(1)
        break

    # Error, wrong input. Restarts the loop
    else:
        print("Invalid input! Try again")
        wait_for_keypress()
# Just doing some    testing