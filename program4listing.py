# Chrissi Federle
# CS115-19Z2
# Spring 2021
# Programming Assignment #4
#
# Program Description
#
# This program will accept, from the user, the starting day of the month named
# as one of 15 elements, and the number of days in said month all subject to
# certain reservations. Then it will display a summary statement inclduing the
# user entered information and an example of the calendar for the month
# corresponding to that user given information. The program will then ask the
# user if they would like to create another calendar. If the answer is 'yes' the
# program will restart, if the answer is 'no' the program will end.
#
# Program Preconditions
#
# 1. The user will enter the starting day of the month, to be called
#    user_start_day_of_month, which must be a string called Hydrogenday,
#    Heliumday, Lithiumday, Berylliumday, Boronday, Carbonday, Nitrogenday,
#    Oxygenday, Fluorineday, Neonday, Sodiumday, Magnesiumday, Aluminumday,
#    Siliconday, or Phosphorusday with exceptions.
#
# 2. The user will enter the number of days in the month, to be called
#    user_days_in_month, which must be a whole number between 42 and 95.
#
# 3. The program will check the range of each input value and adjust it if
#    necessary. It will also check the day of week input and continue to ask
#    until a proper day of the week is entered.
#
# Program Postconditions
#
# 1. The program will display a statement of the starting day of the month, to
#    be called user_start_day_of_month, and the number of days in the month, to
#    be called user_days_in_month.
#
# 2. The program will display an example calendar of the month where the user
#    chose the starting day of the month to be called start in the main function
#    and user_start_day_of_month in the day_name() function. The month will also
#    have the number of days that the user entered between 42 and 95 to be
#    called user_days_in_month in the number_days() function, number in the
#    main() function to begin and finally calendar_days once the function has
#    run.


# Variable Dictionary
#
#
# user_start_day_of_month                    the starting day of the month, as
#                                            given by the user.
#
# user_days_in_month                         the number of days in the month,
#                                            as given by the user.
#
# start                                      the argument from the main()
#                                            function being passed to the
#                                            day_name() function.
#
# number                                     the argument from the main()
#                                            function being passed to the
#                                            number_days() function.
#
# index_number_of_day                        the index placement number of the
#                                            user chosen day of the week.
#
# calendar_days                              the user input of the number of
#                                            days after running the number_days
#                                            () function.
#
# run_again_question                         a yes or no question asking if the
#                                            user wants to create another
#                                            calendar.

#################
# Input section #
#################

# define the index of names of days of the month
day_options = ['Hydrogenday', 'Heliumday','Lithiumday','Berylliumday',\
'Boronday','Carbonday','Nitrogenday','Oxygenday','Fluorineday','Neonday',\
'Sodiumday','Magnesiumday','Aluminumday','Siliconday','Phosphorusday']


# this function is for receiving the user input for the starting day of the
# month, and verifying it for correctness. It receives the 'start' variable
# from the main function and returns the user_start_day_of_month variable.
def day_name(user_start_day_of_month):
    while True:

# ask for the starting day of the month and return the starting day if valid
        try:
            user_start_day_of_month = day_options.index((input('\nEnter the '
            'starting day of the month: ')).lower().title())
            return user_start_day_of_month

# expands on the choice for the day name and asks the user again
        except ValueError:
            print('\nInvalid starting day, should be one of Hydrogenday, '
            'Heliumday, Lithiumday, Berylliumday, Boronday, Carbonday, '
            'Nitrogenday, Oxygenday, Fluorineday, Neonday, Sodiumday, '
            'Magnesiumday, Aluminumday, Siliconday, or Phosphorusday, try '
            'again.')


# this function is for receiving the user input for the number of days in the
# month, and verifying it for correctness in the bounds of this assignment. It
# receives the 'number' variable from the main function and returns the
# 'user_days_in_month' variable.
def number_days(user_days_in_month):
    while True:

# ask for the number of days in the month and return the number if valid
        try:
            user_days_in_month = int(input('\nEnter the number of days in the '
            'month: '))

# tests for the correct range of days in the month and can ask the user again
            while (user_days_in_month < 42 or user_days_in_month > 95):
                print('\nInvalid number of days, should be 42 to 95, try again'
                '.')
                user_days_in_month = int(input('Enter the number of days in '
                'the month: '))
            return user_days_in_month

# tests that the days entered is a whole number
        except ValueError:
            print('\nInvalid number of days, should be a whole number, try'
            ' again.')


# this function is to ask the user if they would like to create another
# calendar after creating their first. It runs the main() function if the user
# responds with yes and exits the program if the user input is no.
def again():
    while True:
        run_again_question = input('\n\nCreate another calendar? ').lower()
        if run_again_question == 'yes':
            main()
        elif run_again_question == 'no':
            exit()
        else:
            print('\nInvalid response, should be yes or no, try again.')


###################
# Process section #
###################

# This is the main function of the program and runs the number_days and day_name
# functions.
def main():

# assign the argument variables to be passed to the other functions
    start = ''
    number = 1

# call and run the day of the week and number of days functions
    index_number_of_day = int(day_name(start))
    calendar_days = number_days(number)

# print a statement summarizing the calendar to be made
    print('\nBlerpian calendar for month starting on', day_options\
    [index_number_of_day], 'with', calendar_days, 'days\n')

# create the abbreviated list of days for the calendar
    days = ['Hy', 'He', 'Li', 'Be', 'Bo', 'Ca', 'Ni', 'Ox', 'Fl', 'Ne', 'So', \
    'Ma', 'Al', 'Si', 'Ph']

# start counting days on the user entered day of the week
    day_index = days.index(days[index_number_of_day])
    calendar = [days]
    calendar.append(['' for _ in range(day_index)])

# create the days based on user input
    for i in range(0, calendar_days):
        if len(calendar[-1]) == len(days):
            calendar.append([])

        calendar[-1].append(i + 1)

# prints out the lists of each week of the calendar in proper format
    for line in calendar:
        print("".join([f'{str(item):3s}'for item in line]))


##################
# Output section #
##################

# run the main function that prints out the final calendar and summary
# statement
main()

# run the function asking if the user would like to create another calendar
again()
