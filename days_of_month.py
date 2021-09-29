#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sep 2021
# This program gives the number of days
#   of the month based on user input


def main():
    # This function gives the number of days of the months based on user input
    leap_year = ""

    # input
    user_input = input("Enter the number of the month (ex: January = 1): ")

    # process & output
    try:
        user_input = int(user_input)
        if user_input == 1:
            print("January has 31 days.")
        elif user_input == 2:
            # second input
            leap_year = input("Is it in a leap year?: ").lower()
            if leap_year == "yes":
                print("February has 29 days.")
            elif leap_year == "no":
                print("February has 28 days.")
            else:
                print("Invalid Input.")
        elif user_input == 3:
            print("March has 31 days.")
        elif user_input == 4:
            print("April has 30 days.")
        elif user_input == 5:
            print("May has 31 days.")
        elif user_input == 6:
            print("June has 30 days.")
        elif user_input == 7:
            print("July has 31 days.")
        elif user_input == 8:
            print("August has 31 days.")
        elif user_input == 9:
            print("September has 30 days.")
        elif user_input == 10:
            print("October has 31 days.")
        elif user_input == 11:
            print("November has 30 days.")
        elif user_input == 12:
            print("December has 31 days.")
        else:
            print("Invalid Number.")
    except (Exception):
        print("Invalid Input.")

    print("\nDone.")


if __name__ == "__main__":
    main()
