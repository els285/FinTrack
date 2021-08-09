import pandas as pd

class Transactions:
    
    def __init__(self,csv_path):
    
        self.csv_path = csv_path
        self.df = pd.read_csv(self.csv_path)
        self.incomings = self.df[self.df["Credit amount"] == self.df["Credit amount"]]
        self.outgoings = self.df[self.df["Credit amount"] != self.df["Credit amount"]]
        self.expenditure = self.outgoings[(self.outgoings["Transaction Type"] == "DEB") | (self.outgoings["Transaction Type"] == "CSH")]                 
        

    def show_all(self):
        print(self.df) 

    def total_incomings(self):
        return self.incomings["Credit amount"].sum()
        
    def total_outgoings(self):
        return self.outgoings["Debit Amount"].sum()

    def total_expenditure(self):
        return self.expenditure["Debit Amount"].sum()
