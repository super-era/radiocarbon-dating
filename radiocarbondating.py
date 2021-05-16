"""
This program asks the user for the percentage of carbon-14 remaining in their sample. 
It then calculates the estimated age of the sample based on the C14 percentage, and
calculates this age in the Common Era format.
"""

import math

# constant for carbon-14 decay formula
k = (math.log(1/2))/5700

# current year
CURRENT_YEAR = 2021


def main():
    # setting up the program to loop so that the user doesn't need
    # to re-initialise the program for every sample
    while True:
        # ask user for input
        remaining_carbon = input("What is the % of C14 remaining in your sample? Enter 'x' to quit. ")

        # setting up the program exit method with an if/else statement
        if remaining_carbon == 'x':
            break

        # setting up the branch where the user input is used to calculate the sample's age
        time_in_years = calculate_sample_age(float(remaining_carbon))

        # rounding the number of years to one decimal place as learnt from tutor Shai! #Section116
        time_in_years = round(time_in_years, 1)

        str_common_era_year = calculate_age_in_CE(time_in_years)

        # return answer to user
        print("Your sample is around " + str(time_in_years) + " years old.")
        print("That means your sample is from around " + str_common_era_year + "!")
        print()   # blank line between program answers for clarity

def calculate_sample_age(remaining_carbon):
    # c14 decay formula solved for time in years: 
    # more info here http://www.biology.arizona.edu/biomath/tutorials/applications/CarbonQ4t.html
    # and here http://www.biology.arizona.edu/biomath/tutorials/applications/carbon.html
    return math.log(remaining_carbon/100)/k

def calculate_age_in_CE(time_in_years):
    # calculating the year in CE that the sample would have come from, and converting to BCE if needed
    common_era_year = CURRENT_YEAR - int(time_in_years)
    if common_era_year < 0:
        str_common_era_year = str(-common_era_year) + " BCE"
    else:
        str_common_era_year = str(common_era_year + 1) + " CE"      # plus 1 because there is no 0CE
    return str_common_era_year


if __name__ == '__main__':
    main()
