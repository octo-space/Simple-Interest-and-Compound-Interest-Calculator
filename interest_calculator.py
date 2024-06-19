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
