# Periodic_table_calendar
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
