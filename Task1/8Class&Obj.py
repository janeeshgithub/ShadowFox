# Task 1: List of Friends and Name Lengths
friends = ["Alice", "Bob", "Charlie", "David", "Eleanor"]
name_lengths = [(friend, len(friend)) for friend in friends]
print("Friend Name Lengths:", name_lengths)

# Task 2: Tracking Expenses
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

# Calculate total expenses
your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

print("Your Total Expenses:", your_total)
print("Partner's Total Expenses:", partner_total)

# Determine who spent more
if your_total > partner_total:
    print("You spent more.")
elif partner_total > your_total:
    print("Your partner spent more.")
else:
    print("Both spent the same amount.")

# Finding the largest spending difference
differences = {category: abs(your_expenses[category] - partner_expenses[category]) for category in your_expenses}
largest_diff_category = max(differences, key=differences.get)
print(f"Largest spending difference: {largest_diff_category} by {differences[largest_diff_category]}")
