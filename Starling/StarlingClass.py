import requests
import datetime


BASE_PATH = "https://api.starlingbank.com/api/v2/"

class StarlingAccount:


    def access_account_details(self):
        return requests.get(BASE_PATH + "accounts", headers=self.headers)

    def __init__(self,PAT,**kwargs):
        self.PAT = PAT
        self.headers =  {"Authorization": "Bearer " + PAT}
        self.requests_object = self.access_account_details()
        self.account_details = self.requests_object.json()['accounts'][0]
        self.accountUid      = self.account_details['accountUid']
        self.defaultCAtegory = self.account_details['defaultCategory']