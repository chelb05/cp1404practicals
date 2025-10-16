"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def print_income_report(incomes, number_of_months):  # Create a new function for printing the report.
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

def main():
    list_of_incomes = []  # Fix the naming for incomes and income.
    number_of_months = int(input("How many months? ")) # Fix naming for month and months.

    for month in range(1, number_of_months + 1):
        income = int(input(f"Enter income for month {month}: "))
        list_of_incomes.append(income)

    print_income_report(list_of_incomes, number_of_months)

main()