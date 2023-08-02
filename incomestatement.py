### Author: Oluwafemi Olasegiri
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
        self.revenue_growth_percent = [] #working cal_revenue_growth_percent
        self.cogs_percent_of_revenue = [] #working cal_cogs_percent_of_revenue
        self.gross_profit_margin = [] #working cal_gross_profit_margin
        self.interest_expense = [] #
        self.interest_income = [] #
        self.net_interest_expense = [] #


    def cal_revenue_growth_percent(self):
        if len(self.revenue) > 0:
            acc = 0
            i = 0
            while(i < len(self.revenue)):
                if i == 0:
                    self.revenue_growth_percent.append(acc)
                else:
                    current_revenue = self.revenue[i]
                    last_revenue = self.revenue[i-1]
                    acc = (current_revenue/last_revenue * 100) - 100
                    self.revenue_growth_percent.append(round(acc, 1))
                i += 1


    def cal_cogs_percent_of_revenue(self):
        if len(self.revenue) == len(self.cogs):
            acc = 0
            i = 0
            while(i < len(self.revenue)):
                acc = self.cogs[i] / self.revenue[i] * 100
                self.cogs_percent_of_revenue.append(round(acc, 1))
                i += 1


    def cal_gross_profit_margin(self):
        if len(self.revenue) == len(self.gross_profit):
            acc = 0
            i = 0
            while(i < len(self.revenue)):
                acc = self.gross_profit[i] / self.revenue[i] * 100
                self.gross_profit_margin.append(round(acc, 1))
                i += 1


    def cal_net_interest_expense(self):
        pass


    def cal_tax_rate(self):
        pass


    def cal_net_margin_percent(self):
        pass


    def cal_net_income_growth(self):
        pass



revenue = [160.0, 170.0, 180.0, 190.0, 200.0]
cogs = [67.2, 70.6, 73.8, 77.9, 80.0]
gross_profit = [92.8, 99.5, 106.2, 112.1, 120.0]
depreciation = [5.0, 5.0, 5.0, 5.0, 5.0]
amortization = [0.0, 0.0, 0.0, 0.0, 0.0]
sga_expenses = [48.0, 51.0, 54.0, 57.0, 60.0]

incomestatement1 = IncomeStatement(revenue, cogs, gross_profit, depreciation, amortization, sga_expenses)
incomestatement1.cal_revenue_growth_percent()
incomestatement1.cal_cogs_percent_of_revenue()
incomestatement1.cal_gross_profit_margin()
print("revenue growth:")
print(incomestatement1.revenue_growth_percent)
print("cogs %\ of revenue:")
print(incomestatement1.cogs_percent_of_revenue)
print("gross profit margin:")
print(incomestatement1.gross_profit_margin)