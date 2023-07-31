def calculate_income_statement(revenue, cost_of_goods_sold, operating_expenses, depreciation, interest_expense, tax_rate):
    """
    Calculate the line items in an Income Statement.

    Ther  Parameters:
    revenue (float): Total revenue for the period.
    cost_of_goods_sold (float): Cost of goods sold for the period.
    operating_expenses (float): Total operating expenses for the period.
    depreciation (float): Depreciation expense for the period.
    interest_expense (float): Interest expense for the period.
    tax_rate (float): Effective tax rate as a decimal (e.g., 0.25 for 25%).

    Returns:
    dict: A dictionary containing the calculated line items in the Income Statement.
    """
    gross_profit = revenue - cost_of_goods_sold
    operating_income = gross_profit - operating_expenses
    ebitda = operating_income + depreciation
    interest_income = 0  # You can include this if applicable
    pre_tax_income = ebitda - interest_expense + interest_income
    income_tax = pre_tax_income * tax_rate
    net_income = pre_tax_income - income_tax

    income_statement = {
        "Revenue": revenue,
        "Cost of Goods Sold": cost_of_goods_sold,
        "Gross Profit": gross_profit,
        "Operating Expenses": operating_expenses,
        "Operating Income": operating_income,
        "EBITDA": ebitda,
        "Interest Expense": interest_expense,
        "Interest Income": interest_income,
        "Pre-Tax Income": pre_tax_income,
        "Income Tax": income_tax,
        "Net Income": net_income
    }

    return income_statement