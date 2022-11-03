class User:

    def __init__(self, lamt, ir, file):
        # loan amount, interest rate, and file attributes respectively
        self.lamt = input('Enter the amount of the loan: ')
        self.ir = input('Enter annual interest rate: ')
        self.file = input('Name of the file you want your results written to: ')

    def show(self):
        print(self.lamt, self.ir, self.file)
