def calculate_annualized_return(start_price, end_price, years):
    """
    Calculate the annualized return between two prices over a given number of years.

    Parameters:
        start_price (float): The starting price.
        end_price (float): The ending price.
        years (int or float): The number of years.

    Returns:
        float: The annualized return as a decimal.
    """
    return (end_price / start_price) ** (1 / years) - 1

# Hardcoded values
start_price_2019 = 150   # Basket price in Dec 2019
end_price_2023 = 179     # Basket price in Dec 2023
end_price_2024 = 254     # Basket price in Dec 2024

# Time periods
years_2019_to_2023 = 4
years_2019_to_2024 = 5
years_2023_to_2024 = 1

# Annualized returns
annualized_return_2019_to_2023 = calculate_annualized_return(start_price_2019, end_price_2023, years_2019_to_2023)
annualized_return_2019_to_2024 = calculate_annualized_return(start_price_2019, end_price_2024, years_2019_to_2024)

# Calculate return for 2023 to 2024 using the derived formula
r_2023_to_2024 = ((1 + annualized_return_2019_to_2024) ** 5 / (1 + annualized_return_2019_to_2023) ** 4) - 1

# Print results
print(f"Annualized return (2019–2023): {annualized_return_2019_to_2023 * 100:.2f}%")
print(f"Annualized return (2019–2024): {annualized_return_2019_to_2024 * 100:.2f}%")
print(f"Annualized return (2023–2024): {r_2023_to_2024 * 100:.2f}%")
