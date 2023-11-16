#Gather the number of books purchased for the month from user input
print("Enter number of books purchased this month: ")
num_books = int(input())

#If-else logic branches for the awards granted for each level of books
#purchased
if (num_books >= 0) and (num_books < 2):
	award_points = 0
elif (num_books >= 2) and (num_books < 4):
	award_points = 5
elif (num_books >= 4) and (num_books < 6):
	award_points = 15
elif (num_books >= 6) and (num_books < 8):
	award_points = 30
elif (num_books >= 8):
	award_points = 60

#Output the points awarded based on the books purchased
print(f"Number of points awarded for this month: {award_points}")