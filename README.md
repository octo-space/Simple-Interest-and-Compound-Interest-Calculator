# 💰 Interest Calculator 💰

This Python script is a simple calculator for both simple and compound interest. 🧮

$[Example Image](example.png)

## Features:

- Calculates simple interest. 🧮
- Calculates compound interest. 📈
- Prompts the user to input the principal amount, interest rate, and time period. 📝
- Displays the calculated results for both simple and compound interest, along with the total amount for each. 📊

## Usage:

1. Save the code as a Python file (e.g., `interest_calculator.py`).
2. Run the script from the command line: `python interest_calculator.py`
3. The script will prompt you for the principal, rate, and time. 
4. Enter the values and the script will display the results. 🎉

## Example:

```
Principal :1000
Rate :5
Time(Year) :3

--- Interest Calculation Results ---
Principal Amount: $1000.00
Interest Rate: 5.00%
Time Period: 3.0 years

Simple Interest: $150.00
Total Amount (Simple): $1150.00

Compound Interest: $157.63
Total Amount (Compound): $1157.63
```

## Code:

```python
def interest_calculator():

    principal  =  float(input("Principal :"))
    rate  =  float(input("Rate :"))
    time  =  float(input("Time(Year) :"))

    # simple interest 
    simple_interest = (principal * rate * time) / 100
    total_amount_simple = principal + simple_interest

    # compund interest 
    compound_interest = principal * (pow((1 + rate / 100), time) - 1)
    total_amount_compound = principal + compound_interest

    # Display the results
    print("\n--- Interest Calculation Results ---")
    print(f"Principal Amount: ${principal:.2f}")
    print(f"Interest Rate: {rate:.2f}%")
    print(f"Time Period: {time} years")
    print(f"\nSimple Interest: ${simple_interest:.2f}")
    print(f"Total Amount (Simple): ${total_amount_simple:.2f}")
    print(f"\nCompound Interest: ${compound_interest:.2f}")
    print(f"Total Amount (Compound): ${total_amount_compound:.2f}")


if __name__ == "__main__":
    interest_calculator()
```

## License:

This project is licensed under the MIT License - see the LICENSE file for details. 📄
