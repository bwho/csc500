print("Enter number of years of rainfall records to enter:")
num_years = int(input())

months_per_year = 12
total_rainfall = 0

year = 1
while year <= num_years:
    month = 1
    while month <= months_per_year:
        print(f"Enter rainfall for year {year}, month {month}: ")
        total_rainfall += int(input())
        month += 1
    year += 1

avg_rainfall = 0
avg_rainfall = total_rainfall / (num_years * months_per_year)

print(f"Total number of months: {num_years * months_per_year}")
print(f"Total inches of rainfall: {total_rainfall}")
print(f"Average rainfall during this time: {avg_rainfall}")