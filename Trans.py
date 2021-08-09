import pandas as pd

class Top:


    def Convert_DateTimes(self):
        from datetime import datetime 
        self.df["Transaction date"]=self.df["Transaction date"].map(lambda x: datetime.strptime(x,'%Y-%m-%d'))

    def Compute(self):
        self.incomings = self.df[self.df["Credit amount"] == self.df["Credit amount"]]
        self.outgoings = self.df[self.df["Credit amount"] != self.df["Credit amount"]]
        self.expenditure = self.outgoings[(self.outgoings["Transaction Type"] == "DEB") | (self.outgoings["Transaction Type"] == "CSH")]                 
        self.transfers_out = self.outgoings[self.outgoings["Transaction Type"]=="FPO"]
        self.transfers_in  = self.incomings[self.incomings["Transaction Type"]=="FPI"]


    def show_all(self):
        with pd.option_context('display.max_rows', None):#::, 'display.max_columns', None):  # more options can be specified also
            print(self.df)

    def total_incomings(self):
        return self.incomings["Credit amount"].sum()
        
    def total_outgoings(self):
        return self.outgoings["Debit Amount"].sum()

    def total_expenditure(self):
        return self.expenditure["Debit Amount"].sum()


class Transactions_FromCSV(Top):

    def __init__(self,csv_path):
         
        self.csv_path = csv_path
        self.df = pd.read_csv(self.csv_path)
        self.Convert_DateTimes()
        self.Compute()
         

class Transactions_Combined(Top):

    def __init__(self,list_of_t):

        self.df = pd.concat([x.df for x in list_of_t])
        self.Compute()
        self.df = self.df.sort_values(by="Transaction date",ascending=False)
