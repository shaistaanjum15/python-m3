import calendar

print(list(calendar.month_name)[1:])
# Ask the user to enter a month number (1 to 12)
month_num = int(input("Enter month number (1-12): "))

# Check if the number is valid and print the month name
if 1 <= month_num <= 12:
  print("The month is:", calendar.month_name[month_num])
else:
  print("Invalid input! Please enter a number between 1 and 12.")