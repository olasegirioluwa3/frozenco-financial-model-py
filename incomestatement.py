###
### IncomeStatement
### 
class IncomeStatement:
    tax_rate = 0
    def __init__(self, revenue, cogs, gross_profit, depreciation, amortization, sga_expenses):
        self.revenue = revenue
        self.cogs = cogs
        self.gross_profit = gross_profit
        self.depreciation = depreciation
        self.amortization = amortization
        self.sga_expenses = sga_expenses
        self.other_income_expense = []
        self.revenue_growth_percent = []
        self.cogs_percent_of_revenue = []
        self.gross_profit_margin = []
        self.interest_expense = []
        self.interest_income = []
        self.net_interest_expense = []


    def get_revenue(self):
        return self.revenue
    
    def cal_revenue_growth_percent(self):
        if len(self.total_current_assets) == 0:
            acc = 0
            i = 0
            while(i < len(self.total_current_assets)):
                acc = self.total_current_assets[i] + self.netppe[i] + self.other_assets[i] + self.goodwill[i]
                self.total_assets.append(acc)
                i += 1


    def get_cogs(self):
        return self.cogs
    


revenue = [160.0, 170.0, 180.0, 190.0, 200.0]
cogs = [67.2, 70.6, 73.8, 77.9, 80.0]
gross_profit = [92.8, 99.5, 106.2, 112.1, 120.0]
depreciation = [5.0, 5.0, 5.0, 5.0, 5.0]
amortization = [0.0, 0.0, 0.0, 0.0, 0.0]
sga_expenses = [48.0, 51.0, 54.0, 57.0, 60.0]

incomestatement1 = IncomeStatement(revenue, cogs, gross_profit, depreciation, amortization, sga_expenses)