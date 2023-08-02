import assets

class App:
    def __init__(self):
        appinput = input()
        check = appinput.isnumeric()
        if check:
            print('its a number')
        else:
            print("invalid input")
        pass


app1 = App()
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