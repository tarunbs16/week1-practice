expenses = [250, 1200, 450, 800, 150, 2000, 350]

total_expense = sum(expenses)
average_expense = total_expense / len(expenses)
highest_expense = max(expenses)
lowest_expense = min(expenses)

above_500_count = sum(1 for exp in expenses if exp > 500)
below_equal_500_count = sum(1 for exp in expenses if exp <= 500)

print(f"Total Expense: {total_expense}")
print(f"Average Expense: {average_expense:.2f}")
print(f"Highest Expense: {highest_expense}")
print(f"Lowest Expense: {lowest_expense}")
print(f"Number of Expenses Above ₹500: {above_500_count}")
print(f"Number of Expenses Below or Equal to ₹500: {below_equal_500_count}")

print("\nExpenses Above Average:")
for exp in expenses:
    if exp > average_expense:
        print(exp)
