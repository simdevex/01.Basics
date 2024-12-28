from scipy.optimize import fsolve

def calculate_interest_rate_for_weekly_instalment():
    """
    Calculate the annual interest rate required for a weekly mortgage installment of $550.
    """
    # Hardcoded values based on your scenario
    weekly_instalment = 550  # Desired weekly installment in dollars
    mortgage_amount = 577000  # Loan amount in dollars
    loan_term_years = 30  # Loan term in years
    weeks_per_year = 52  # Number of weeks in a year
    total_weeks = loan_term_years * weeks_per_year  # Total number of payments in weeks

    # Convert weekly installment to equivalent monthly installment
    monthly_instalment = (weekly_instalment * weeks_per_year) / 12

    def equation_to_solve(annual_interest_rate):
        """
        Equation for the monthly installment as a function of interest rate.
        """
        monthly_interest_rate = (annual_interest_rate / 100) / 12  # Monthly interest rate
        total_months = loan_term_years * 12  # Total number of payments in months
        return mortgage_amount * monthly_interest_rate * (1 + monthly_interest_rate)**total_months / \
               ((1 + monthly_interest_rate)**total_months - 1) - monthly_instalment

    # Initial guess for the annual interest rate
    initial_guess = 5.0  # Percentage

    # Solve for the annual interest rate using fsolve
    interest_rate_solution = fsolve(equation_to_solve, initial_guess)[0]

    # Display the result
    print(f"The required annual interest rate for a weekly installment of ${weekly_instalment} is: {interest_rate_solution:.2f}%")

# Run the calculation
calculate_interest_rate_for_weekly_instalment()
