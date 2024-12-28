def calculate_weekly_instalment():
    """
    Calculate the weekly mortgage installment for the given scenario.
    """
    # Hardcoded values based on your scenario
    mortgage_amount = 577000  # Loan amount in dollars
    annual_interest_rate = 6.29  # Annual interest rate in percentage
    loan_term_years = 30  # Loan term in years

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Total number of payments (months)
    total_months = loan_term_years * 12

    # Monthly installment formula (EMI)
    # EMI = P * r * (1 + r)^n / ((1 + r)^n - 1)
    P = mortgage_amount
    r = monthly_interest_rate
    n = total_months

    monthly_instalment = P * r * ((1 + r)**n) / (((1 + r)**n) - 1)

    # Convert monthly installment to weekly (assuming 52 weeks per year)
    weekly_instalment = (monthly_instalment * 12) / 52

    # Display the result
    print(f"Your weekly mortgage installment is: ${weekly_instalment:.2f}")

# Run the calculation
calculate_weekly_instalment()
