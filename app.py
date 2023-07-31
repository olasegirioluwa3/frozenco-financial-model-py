class IncomeStatement:

    tax_rate = 0
    def __init__(self, revenue, cogs, grossppe, amortization, sga_sales, other_income_expense):
        self.revenue = revenue
        self.cogs = cogs
        self.grossppe = grossppe
        self.amortization = amortization
        self.sga_sales = sga_sales
        self.other_income_expense = other_income_expense

    def get_revenue(self):
        return self.revenue
    
    def get_cogs(self):
        return self.cogs
    
    def get_depreciation_gross_ppe(self):
        return self.grossppe
    
    def get_grossppe(self):
        return self.amortization
    
    def get_sga_sales(self):
        return self.sga_sales
    
    def get_other_income_expense(self):
        return self.other_income_expense
    

class BalanceSheet:

    tax_rate = 0
    def __init__(self, cash, accounts_receivable, inventory, other_current_assets):
        self.cash = cash
        self.accounts_receivable = accounts_receivable
        self.inventory = inventory
        self.other_current_assets = other_current_assets

    def total_current_assets(self):
        #iterate and return 
        pass

    