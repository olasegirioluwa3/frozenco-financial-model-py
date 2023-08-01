###
### BalanceSheet -> Assets
### This is a working class

class Assets:
    def __init__(self, cash, accounts_receivable, inventory, other_current_assets, grossppe, accummulated_depreciation, other_assets, goodwill):
        self.cash = cash
        self.accounts_receivable = accounts_receivable
        self.inventory = inventory
        self.other_current_assets = other_current_assets
        self.grossppe = grossppe
        self.accummulated_depreciation = accummulated_depreciation
        self.other_assets = other_assets
        self.goodwill = goodwill
        self.total_current_assets = []
        self.netppe = []
        self.total_assets = []

    def cal_total_current_assets(self):
        #iterate and return 
        if len(self.cash) == len(self.accounts_receivable) == len(self.inventory) == len(self.other_current_assets):
            acc = 0
            i = 0
            while(i < len(self.cash)):
                acc = self.cash[i] + self.accounts_receivable[i] + self.inventory[i] + self.other_current_assets[i]
                self.total_current_assets.append(acc)
                i += 1
        

    def cal_netppe(self):
        if len(self.grossppe) == len(self.accummulated_depreciation):
            acc = 0
            i = 0
            while(i < len(self.grossppe)):
                acc = self.grossppe[i] - self.accummulated_depreciation[i]
                self.netppe.append(acc)
                i += 1


    def cal_total_assets(self):
        if len(self.total_current_assets) == len(self.netppe) == len(self.other_assets) == len(self.goodwill):
            acc = 0
            i = 0
            while(i < len(self.total_current_assets)):
                acc = self.total_current_assets[i] + self.netppe[i] + self.other_assets[i] + self.goodwill[i]
                self.total_assets.append(acc)
                i += 1


#initialize data
cash = [5.0, 0.0, 0.0, 0.0, 0.0]
accounts_receivable = [12.0, 13.0, 14.0, 15.0, 16.0]
inventory = [8.0, 8.5, 9.0, 9.5, 10.0]
other_current_assets = [1.0, 1.0, 1.0, 1.0, 1.0]
grossppe = [277.2, 287.2, 298.2, 310.2, 323.2]
accummulated_depreciation = [25.0, 30.0, 35.0, 40.0, 45.0]
other_assets = [0.0, 0.0, 0.0, 0.0, 0.0]
goodwill = [5.0, 5.0, 5.0, 5.0, 5.0]

#initialize Asset class
asset1 = Assets(cash, accounts_receivable, inventory, other_current_assets, grossppe, accummulated_depreciation, other_assets, goodwill)
asset1.cal_total_current_assets()
asset1.cal_netppe()
print("Total Current Assets:")
print(asset1.total_current_assets)
print("NetPPE:")
print(asset1.netppe)
asset1.cal_total_assets()
print("Total Assets:")
print(asset1.total_assets)