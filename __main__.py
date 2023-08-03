from incomestatement import IncomeStatement
import matplotlib.pyplot as plt
class App(IncomeStatement):
    def __init__(self):
        self.incomestatement1 = IncomeStatement()
        print("")
        print("Frozen Co. Business Support (CareerOnDemand)")
        print("")
        print("")
        print("Hello, I am FemiPY, your friendly business support BOT")
        print("I will be here to help you uncover the secrets from your business data")
        print("")
        print("Select any of the options below to get started")
        print("1 ====> Revenue")
        print("2 ====> Revenue Growth")
        presentation_option = input()
        check = presentation_option.isnumeric()
        
        if check:
            if presentation_option == '1':
                self.present_revenue()
            if presentation_option == '2':
                self.present_revenue_growth()
        else:
            print("Sorry, I could not process your request")


    def present_revenue(self):
        #initialize Asset class
        print("Revenue Presentation")
        plt.plot(IncomeStatement.get_total_year(self.incomestatement1), IncomeStatement.get_revenue(self.incomestatement1))
        plt.xlabel('Fiscal Year')
        plt.ylabel('Revenue in Million Dollars')
        plt.title('FROZEN CO. FINANCIALS (REVENUE)')
        plt.show()


    def present_revenue_growth(self):
        #initialize Asset class
        print("Revenue Growth Presentation")
        
        plt.plot(IncomeStatement.get_total_year(self.incomestatement1), IncomeStatement.cal_revenue_growth_percent(self.incomestatement1))
        plt.xlabel('Fiscal Year')
        plt.ylabel('Revenue growth in %')
        plt.show()

app1 = App()
