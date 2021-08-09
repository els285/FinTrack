# Generate practice transactions csv in the style of TSB
import datetime
import pandas as pd
import random

def Random_Transaction_CSV(number_of_transactions,name):

    columns = ["Transaction date",
                "Transaction Type",
                "Sort Code",
                "Account Number",
                "Transaction description",
                "Debit Amount",
                "Credit amount",
                "Balance"]

    df = pd.DataFrame(columns=columns)

    def random_date(start_date,end_date):
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        return random_date

    # Do dates
    start_date = datetime.date(2000, 1, 1)
    end_date   = datetime.date.today()
    dts = [random_date(start_date,end_date) for i in range(0,number_of_transactions)]

    # Generate types
    trans_types=['DEB', 'FPI', 'TFR', 'CSH', 'DD', 'DC', 'CHQ', 'FPO']
    trans_weights = [0.5, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05, 0.1]
    types=random.choices(population=trans_types,weights=trans_weights,k=number_of_transactions)

    AMs = ['12345678']*number_of_transactions
    sorts = ['01-23-45']*number_of_transactions

    import requests
    import math


    def random_list_of_words(N):
        word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
        response = requests.get(word_site)
        WORDS = response.content.splitlines()

        w = []
        for i in range(0,N):
            wl = [x.decode("utf-8") for x in random.sample(WORDS,random.randint(1,4))]
            wl2 = ""
            for x in wl:
                wl2 += x + " "
            w.append(wl2)
        return w


    def random_amount():
        return round(random.uniform(-300,300),2)

    def the_money(N):

        balance_list = []
        balance = random_amount()
        credit,debit = [],[]
        for i in range(0,N):
            v = random_amount()
            if v >=0:
                credit.append(v)
                debit.append(math.nan)
            if v <0:
                credit.append(math.nan)
                debit.append(-v)

            balance += v
            balance_list.append(balance)

        return credit,debit,balance_list


    credit,debit,balance_list = the_money(number_of_transactions)

    df["Transaction date"]        = dts
    df["Transaction Type"]        = types
    df["Sort Code"]               = sorts
    df["Account Number"]          = AMs
    df["Transaction description"] = random_list_of_words(number_of_transactions)
    df["Debit Amount"]            = debit
    df["Credit amount"]           = credit
    df["Balance"]                 = balance_list

    df.to_csv(name,index=False)


Random_Transaction_CSV(100,"./rand_trans.csv")






            