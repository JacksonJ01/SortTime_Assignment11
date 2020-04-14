from Search_Methods import *
from time import time, sleep
from random import randint
numbers = []

input("*PRESS ENTER*")
sleep(1)

print("\nGreetings, looks like you enjoyed the last program I showed you."
      "\nWell, guess what! "
      "\nYou're in luck, because I have another one just like it."
      "\nToday we are going to calculate the time it takes the chosen sort method to complete a sort")
# sleep(2.5)

start = input("\nLike last time, if you would like to see the program, you must type 'start'."
              "\n>>>").title()

fails = 0
while start != "Start":
    start = input("\nType 'start' please"
                  "\n>>>").title()
    fails += 1
    # sleep(.25)

# For added sass
if fails >= 3:
    print("\nFinally...")

print("Alight, let's get this show on the road.\n\n")

menu = "Hello World"
while menu != "EXIT":
    # sleep(1.5)
    print("_" * 100)
    print("\n_Press The Number Next To Your Desired Choice_")

    # The user can choose the sort method they would like to use
    menu = input("\n   -Menu-"
                 "\n1. Bubble Sort"
                 "\n2. Insertion Sort"
                 "\n3. Selection Sort"
                 "\n4. Merge Sort"
                 "\n5. Quick Sort"
                 "\n6. EXIT"
                 "\n>>>")

    while menu != "HW":
        # Tries to save menu as an integer. If a string is entered the code won't fail due to a .int value error
        try:
            menu = int(menu)
            break
        except ValueError:
            menu = input("\nWhat number did you attempt to type?"
                         "\n>>>")

    if menu == 6:
        print("\nThanks for playing")
        quit()

    # sleep(.5)
    # The user can choose between 'preset' values, or they can enter their own
    menu2 = input("\nHow many numbers would you like to see this method sort?"
                  "\n1. 20,000 numbers"
                  "\n2. 50,000 numbers"
                  "\n3. 100,000 numbers"
                  "\n4. Custom Value"
                  "\n>>>")

    while menu2 != "Hw":
        # checks if the value entered is a number
        try:
            menu2 = int(menu2)
        except ValueError:
            print('\nChoose a number in front of your desired choice please'.title(),
                  '\n>>>')

        # I use a for loop to append to the list and I found it easier to just append menu2
        # instead of doing a loop for each value
        if menu2 == 1:
            menu2 = 20000

        elif menu2 == 2:
            menu2 = 50000

        elif menu2 == 3:
            menu2 = 100000

        elif menu2 == 4:
            sort = input("\nHow many values?"
                         "\n>>>")

            while sort == "HW":
                # checks if they entered a number
                try:
                    menu2 = int(sort)
                except ValueError:
                    sort = input("\nHow many values would you like to see this method sort?")

        # sleep(1)
        # Appends the values to the list
        for number in range(0, menu2):
            numbers.append(randint(1, 100000))

        print(f"\nAll {menu2} items have been added into the list.")
        # 100,000 items in a list is a lot, so I ask the user, before randomly plopping the items on to their screen
        see = input("Would you like to see the numbers? (Y or N)"
                    "\n>>>").title()

        if see == "Y" or see == "Yes":
            # If they want to see 100 numbers, it's not that bad, so I have this text for longer lists
            if menu2 >= 3000:
                print("Brace yourself:")
            print("Press Enter when you're done.")
            # sleep(1.5)
            print(numbers)
            # I don't want the code to just continue while the user looks at the values,
            # so they have to press enter when they're done
            input("press enter to continue".upper())

        print("Alright, I'm running it:")
        # sleep(.5)
        countdown = 3
        for down in range(0, 3):  # I definitely could have put this in a multiple print statement but..
            print(countdown)
            countdown -= 1
            # sleep(1)
        print("Gooo!")

        start_time = "HW"  # I have this in each if statement because if the user chooses quick_sort,
                           # the code will spend time moving to that last if statement and it won't be exact
        if menu == 1:
            start_time = time()
            arranged = Bubble_Sort(numbers)

        if menu == 2:
            start_time = time()
            arranged = Insertion_Sort(numbers)

        if menu == 3:
            start_time = time()
            arranged = Selection_Sort(numbers)

        if menu == 4:
            start_time = time()
            arranged = Merge_Sort(numbers)

        if menu == 5:
            start_time = time()
            arranged = Quick_Sort(numbers)

        total_time = time() - start_time
        print("\nAnd TIME!!"
              f"\nIt took {total_time: 8f} seconds for the method to finish sorting, (I only included 8 values after the decimal place).")

        see = input("Would you like to see the sorted list? (Y or N)").title()
        if see == "Y" or see == "Yes":
            if menu2 >= 3000:
                print("Once again, brace yourself:")
            # sleep(1.5)
            print(numbers)
            input('press enter to continue'.upper())

        print('\nAlright, I\'m taking you back to the menu, where you can play around some more, or leave..'
              '\nBut you don\'t have to leave')
        # sleep(.5)
