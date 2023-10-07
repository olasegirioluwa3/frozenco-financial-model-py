### Author: Oluwafemi Olasegiri
### IncomeStatement
### 
class IncomeStatement:
    "tax_rate = 40.0 #tax rate after data"
    revenue_growth_rate = 5.0 #revenue growth after data
    def __init__(self):
        self.year = [2012, 2013, 2014, 2015, 2016]
        self.revenue = [160.0, 170.0, 180.0, 190.0, 200.0]
        self.cogs = [67.2, 70.6, 73.8, 77.9, 80.0]
        self.gross_profit = [92.8, 99.5, 106.2, 112.1, 120.0]
        self.depreciation = [5.0, 5.0, 5.0, 5.0, 5.0]
        self.amortization = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.sga_expenses = [48.0, 51.0, 54.0, 57.0, 60.0]
        self.other_income_expense = [0.0, 0.0, 0.0, 0.0, 0.0]
        
        self.revenue_growth_percent = self.cal_revenue_growth_percent()
        self.cogs_percent_of_revenue = self.cal_cogs_percent_of_revenue()
        self.gross_profit_margin = self.cal_gross_profit_margin()
        
        self.interest_expense = self.cal_interest_expense()  # Placeholder for interest expense calculation
        self.interest_income = self.cal_interest_income()    # Placeholder for interest income calculation
        self.net_interest_expense = self.cal_net_interest_expense()  # Placeholder for net interest expense calculation



    def get_revenue(self):
        return self.revenue
    

    def get_total_year(self):
        year = 2012
        return [year + i for i in range(len(self.revenue))]
    

    def cal_revenue_growth_percent(self):
        acc_list = [0.0] + [round((self.revenue[i] / self.revenue[i - 1] * 100) - 100, 1) for i in range(1, len(self.revenue))]
        return acc_list
    

    def cal_cogs_percent_of_revenue(self):
        if len(self.revenue) == len(self.cogs):
            acc_list = [round(self.cogs[i] / self.revenue[i] * 100, 1) for i in range(len(self.revenue))]
            return acc_list
        else:
            return []



    def cal_gross_profit_margin(self):
        if len(self.revenue) == len(self.gross_profit):
            acc_list = [round(self.gross_profit[i] / self.revenue[i] * 100, 1) for i in range(len(self.revenue))]
            return acc_list
        else:
            return []



    def cal_tax_rate(self):
        pass


    def cal_net_margin_percent(self):
        pass


    def cal_net_income_growth(self):
        pass


    def get_ebitda(self):
        # (Operating Income / EBIT) / + Depreciation
        pass


    def operating_income_per_ebit(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < len(self.gross_profit)):
            acc = self.gross_profit[i] - self.depreciation[i] - self.amortization[i] - self.sga_expenses[i]
            acc_list.append(round(acc, 1))
            i += 1
        return acc_list


    def operating_income_per_ebit_margin_percent(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < len(self.operating_income_per_ebit())):
            acc = self.operating_income_per_ebit()[i] / self.revenue[i]
            acc_list.append(round(acc, 1))
            i += 1


    def ebitda(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < len(self.operating_income_per_ebit())):
            acc = self.operating_income_per_ebit()[i] + self.depreciation[i] + self.amortization[i]
            acc_list.append(acc)
            i += 1
        return acc_list
    

    def ebitda_margin_percent(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < self.ebitda()):
            acc = self.ebitda()[i] / self.revenue[i]
            acc_list.append(acc)
            i += 1
        return acc_list


    def ebitda_growth(self):
        if len(self.ebitda()) > 0:
            acc = 0
            i = 0
            acc_list = []
            while(i < len(self.ebitda())):
                if i == 0:
                    acc_list.append(0.0)
                else:
                    current_growth = self.ebitda()[i]
                    last_growth = self.ebitda()[i-1]
                    acc = (current_growth/last_growth) - 1
                    acc_list.append(round(acc, 1))
                    #self.revenue_growth_percent.append(round(acc, 1))
                i += 1
        return acc_list
    

    def cal_interest_expense(self):
        return []
    def cal_interest_income(self):
        return []
    

    def cal_net_interest_expense(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < self.cal_interest_expense()):
            acc = self.cal_interest_expense()[i] - self.cal_interest_income()[i]
            acc_list.append(acc)
            i += 1
        return acc_list
    

    def other_income_per_expense(self):
        return [2.0, 0.0, -2.0, 1.0, 0.0]
    

    def pretax_income(self):
        return []
    def taxes(self):
        return []
    def tax_rate(self):
        return []
    def cal_net_income(self):
        return [0.0, 0.0, 0.0, 0.0, 0.0]
    def net_margin_percent(self):
        return []
    def net_income_growth(self):
        return []

class BalanceSheet:
    def __init__(self):
        self.year = [2012, 2013, 2014, 2015, 2016]
        self.cash = self.get_cash()
        self.accounts_receivable = [12.0, 13.0, 14.0, 15.0, 16.0]
        self.inventory = [8.0, 8.5, 9.0, 9.5, 10.0]
        self.other_current_assets = [1.0, 1.0, 1.0, 1.0, 1.0]
        self.goodwill = [5.0, 5.0, 5.0, 5.0, 5.0]

    def get_cash(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < len(self.accounts_receivable)):
            if i == 0:
                acc = 5.0
            else:
                acc = self.cash[i] + self.accounts_receivable[i] + self.inventory[i] + self.other_current_assets[i]
            acc_list.append(acc)
            i += 1
        return acc_list

    def total_current_assets(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < len(self.accounts_receivable)):
            acc = self.cash[i] + self.accounts_receivable[i] + self.inventory[i] + self.other_current_assets[i]
            acc_list.append(acc)
            i += 1
        return acc_list


class CashFlow:
    def __init__(self):
        self.incomestatement1 = IncomeStatement()
        self.net_income = self.cal_net_income()

    def cal_net_income(self):
        acc = 0
        i = 0
        acc_list = []
        """while(i < len(IncomeStatement.cal_cogs_percent_of_revenue())):
            if i == 0:
                acc = 5.0
            else:
                acc = IncomeStatement.cal_interest_income()[i]
            acc_list.append(acc[i])
            i += 1"""
        return acc_list

class DebtIS:
    def __init__(self):
        pass

    "Revolver"
    def beginning_revolver_balance(self):
        pass
    def revolver_paydwon_drawdown(self):
        pass
    def ending_revolver_balance(self):
        pass
    def revolver_interest_rate(self):
        pass
    def revolver_interest_expense(self):
        pass

    "Term Loan"
    def term_loan_beginning_balance(self):
        return []
    def term_loan_paydown_drawdown(self):
        return []
    def term_loan_ending_balance(self):
        return []
    def term_loan_interest_rate(self):
        return []
    def term_loan_interest_expense(self):
        return []
    

    "Unsecured Loan"
    def unsecured_debt_beginning_balance(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < self.unsecured_debt_ending_balance()):
            acc = self.unsecured_debt_ending_balance()[i-1]
            acc_list.append(acc)
            i += 1
        return acc_list
    

    def Unsecured_debt_paydown_drawdown(self):
        return [0.0, 0.0, 0.0, 0.0, 0.0]
    

    def unsecured_debt_ending_balance(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < self.unsecured_debt_beginning_balance()):
            acc = self.unsecured_debt_beginning_balance()[i] + self.Unsecured_debt_paydown_drawdown()[i]
            acc_list.append(acc)
            i += 1
        return acc_list
    def unsecured_debt_interest_rate(self):
        return []
    def unsecured_debt_interest_expense(self):
        return []
    def total_interest_expense(self):
        acc = 0
        i = 0
        acc_list = []
        while(i < self.revolver_interest_expense()):
            acc = self.revolver_interest_expense()[i] + self.term_loan_interest_expense()[i] + self.unsecured_debt_interest_expense()[i]
            acc_list.append(acc)
            i += 1
        return acc_list
    def interest_earned_on_cash(self):
        return []
    




#revenue = [160.0, 170.0, 180.0, 190.0, 200.0]
#cogs = [67.2, 70.6, 73.8, 77.9, 80.0]
#gross_profit = [92.8, 99.5, 106.2, 112.1, 120.0]
#depreciation = [5.0, 5.0, 5.0, 5.0, 5.0]
#amortization = [0.0, 0.0, 0.0, 0.0, 0.0]
#sga_expenses = [48.0, 51.0, 54.0, 57.0, 60.0]

#incomestatement1 = IncomeStatement(revenue, cogs, gross_profit, depreciation, amortization, sga_expenses)
#
#incomestatement1 = IncomeStatement()

#incomestatement1.cal_revenue_growth_percent()
#incomestatement1.cal_cogs_percent_of_revenue()
#incomestatement1.cal_gross_profit_margin()
#print("revenue growth:")
#print(incomestatement1.revenue_growth_percent)
#print("cogs %\ of revenue:")
#print(incomestatement1.cogs_percent_of_revenue)
#print("gross profit margin:")
#print(incomestatement1.gross_profit_margin)
#print("years:")
#print(incomestatement1.get_total_year());
#print(incomestatement1.cogs_percent_of_revenue)
#print("Revenue Presentation")
import matplotlib.pyplot as plt
#plt.plot(incomestatement1.get_total_year(), incomestatement1.revenue)
#
#plt.xlabel('Fiscal Year')
#plt.ylabel('Revenue in Million Dollars')
#plt.title('FROZEN CO. FINANCIALS (REVENUE)')
#plt.show()
#
plt.plot(incomestatement1.get_total_year(), incomestatement1.revenue_growth_percent)
plt.xlabel('Fiscal Year')
plt.ylabel('Revenue growth in %')
plt.show()
