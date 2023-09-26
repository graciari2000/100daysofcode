# Function to calculate the tip amount
def calculate_tip(bill_amount, tip_percentage):
    tip = (bill_amount * tip_percentage) / 100
    return tip

# Function to calculate the total bill amount including the tip
def calculate_total_bill(bill_amount, tip_amount):
    total_bill = bill_amount + tip_amount
    return total_bill

# Main program
try:
    # Input: Bill amount and tip percentage
    bill_amount = float(input("Enter the bill amount: $"))
    tip_percentage = float(input("Enter the tip percentage you'd like to leave (e.g., 15): "))

    # Calculate tip and total bill
    tip_amount = calculate_tip(bill_amount, tip_percentage)
    total_bill = calculate_total_bill(bill_amount, tip_amount)

    # Display results
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total bill including tip: ${total_bill:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values for the bill amount and tip percentage.")