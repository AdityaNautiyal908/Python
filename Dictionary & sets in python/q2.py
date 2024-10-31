months_days = {
    "January" : 31,
    "February" : 28,
    "March" : 31,
    "April" : 30,
    "May" : 31,
    "June" : 30,
    "July" : 31,
    "August" : 31,
    "September" : 30,
    "October" : 31,
    "November" : 30,
    "December" : 31
}

month_input = input("Enter the month name : ").capitalize()

if month_input in months_days:
    print(f"{month_input} has {months_days[month_input]} days.")
else:
    print("Invalid month name.Please try again")


# Step 4 print all the keys in alphabetical order
print("\nMonths in alphabetical order:")
for month in sorted(months_days.keys()):
    print(month)

# Step 5: Print out all month with 31 days
print("\nMonth with 31 days:")
for month,days in months_days.items():
    if days == 31:
        print(month)

# Step 6: Print key-value pairs sorted by the number of days
print("\nMonths sorted by number of days:")
for month in sorted(months_days, key=lambda m: months_days[m]):
    print(f"{month}: {months_days[month]} days")