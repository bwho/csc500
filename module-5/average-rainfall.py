# Gather number of years to collect records for from user input
print("Enter number of years of rainfall records to enter:")
num_years = int(input())

# Set number of months per year and initialize variable to collect rainfall
# amounts 
months_per_year = 12
total_rainfall = 0

# Inititalize counter variable for years and begin to loop through number of
# years
year = 1
while year <= num_years:
    
    #Initialize counter variable for number of months and begin to loop
    #through months. It's important this in within outer loop so that it is
    #reinitialized at the beginning of the next year.
    month = 1
    while month <= months_per_year:

        #Gather the rainfall amount for each month and add to the running total
        print(f"Enter rainfall for Year {year}, Month {month}: ")
        total_rainfall += int(input())

        #Increment the month before the next month loop run
        month += 1

    #Increment the year before the next year loop run
    year += 1

#Compute the average rainfall by dividing by the total number of months
avg_rainfall = total_rainfall / (num_years * months_per_year)

#Output the total number of months, total inches of rainfall collected and the
#Average rainfall per month during this period
print(f"Total number of months: {num_years * months_per_year}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall per month during this period: {avg_rainfall}")